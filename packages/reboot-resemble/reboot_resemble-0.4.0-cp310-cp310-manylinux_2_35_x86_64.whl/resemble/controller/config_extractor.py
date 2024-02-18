import asyncio
import grpc
import kubernetes_asyncio
import uuid
from kubernetes_utils.helpers import WatchEventType
from kubernetes_utils.kubernetes_client import EnhancedKubernetesClient
from kubernetes_utils.ownership import OwnershipInformation
from kubernetes_utils.retry import retry_insecure_grpc_unless_pods_have_failed
from resemble.aio.servicers import Serviceable
from resemble.aio.types import RoutableAddress
from resemble.controller.exceptions import InputError
from resemble.controller.server_config import ServerConfig
from resemble.controller.server_deployment import ServerDeployment
from resemble.controller.settings import (
    APPLICATION_SERVICE_ACCOUNT,
    ENVVAR_RESEMBLE_CONFIG_SERVER_PORT,
    ENVVAR_RESEMBLE_MODE,
    RESEMBLE_MODE_CONFIG,
)
from resemble.helpers import (
    generate_proto_descriptor_set,
    get_server_name_from_service_names,
)
from resemble.v1alpha1 import (
    config_mode_pb2,
    config_mode_pb2_grpc,
    server_config_pb2,
)
from respect.logging import get_logger

logger = get_logger(__name__)

# This hardcoded server port KUBERNETES_CONFIG_SERVER_PORT is safe because
# it will only ever run on Kubernetes where there is no chance of
# a port conflict due to simultaneous tests.
KUBERNETES_CONFIG_SERVER_PORT = 56653

# The name we will assign to the container running inside the config pod.
CONFIG_CONTAINER_NAME = 'config-server'


class LocalConfigExtractor:

    def config_from_serviceables(
        self, serviceables: list[Serviceable]
    ) -> ServerConfig:
        file_descriptor_set = generate_proto_descriptor_set(
            routables=serviceables
        )

        service_names = [s.service_name() for s in serviceables]
        return ServerConfig(
            spec=ServerConfig.Spec(
                server_deployment_name=get_server_name_from_service_names(
                    service_names
                ),
                file_descriptor_set=file_descriptor_set.SerializeToString(),
                container_image_name='local.noop',
                service_names=service_names,
            ),
        )


class KubernetesConfigExtractor:
    # The maximum time to wait for the config pod to come up and the maximum
    # time to wait after that to connect to the pod.
    CONFIG_POD_TIMEOUT_SECONDS = 30

    def __init__(
        self,
        k8s_client: EnhancedKubernetesClient,
    ):
        self._k8s_client = k8s_client

    async def run(self) -> None:
        await self._watch_for_server_deployment_objects()

    async def _watch_for_server_deployment_objects(self) -> None:
        logger.info(
            'Watching for ServerDeployment changes in any namespace...'
        )
        async for watch_event in self._k8s_client.custom_objects.watch_all(
            object_type=ServerDeployment,
        ):

            event_type: WatchEventType = watch_event.type
            logger.debug(
                'ServerDeployment %s: %s',
                event_type,
                watch_event.object.metadata.name or 'Unknown',
            )

            try:
                if event_type in [
                    WatchEventType.MODIFIED, WatchEventType.ADDED
                ]:
                    await self._handle_server_deployment_update(
                        watch_event.object
                    )
                elif event_type == WatchEventType.DELETED:
                    # ISSUE(https://github.com/reboot-dev/respect/issues/1485):
                    # We currently rely on kubernetes object ownership to delete
                    # the custom objects we create. However as the garbage
                    # collector can get overwhelmed and we should proactively
                    # delete our objects. So, here we should actively delete the
                    # `ServerConfig` object corresponding to the now deleted
                    # `ServerDeployment` object.
                    pass
                else:
                    logger.warning(f'Unknown event type: {event_type}')

            except InputError as e:
                # TODO: Report these errors to the developer who wrote the
                # `ServerDeployment`, e.g. by updating the
                # `ServerDeployment.status` field.
                logger.error(
                    'Got custom object error: %s',
                    e.reason,
                )
            except Exception as e:
                # TODO: Report these errors to the developer who wrote the
                # `ServerDeployment` on a best effort basis, e.g. by attempting
                # to update the `ServerDeployment.status` field.
                logger.critical(
                    'Got unknown error for object %s: %s',
                    type(e).__name__,
                    str(e),
                )
                raise

        logger.info('Stopped watching for ServerDeployment changes')

    async def _handle_server_deployment_update(
        self, server_deployment: ServerDeployment
    ) -> None:
        # TODO: do all of this in a background task so we can have more than
        # one config-pod at a time.

        if server_deployment.metadata.name is None:
            raise InputError(
                reason="In 'ServerDeployment': field 'metadata.name' must not "
                "be empty"
            )

        if server_deployment.metadata.namespace is None:
            raise InputError(
                reason=
                "In 'ServerDeployment': field 'metadata.namespace' must not "
                "be empty"
            )

        if server_deployment.spec.container_image_name == '':
            raise InputError(
                reason="In 'ServerDeployment' with name "
                f"'{server_deployment.metadata.name}': field "
                "'container_image_name' must not be empty"
            )

        # Everything we are about to create, delete and update is in this
        # namespace.
        application_namespace = server_deployment.metadata.namespace

        # Come up with a unique name for the config pod. Having a unique name is
        # important, since even if we handle just one ServerDeployment at a time
        # it is possible for an old config pod to still be in state
        # `Terminating`when we want to create the next one.
        config_pod_name = f'config-pod-{uuid.uuid4()}'
        logger.debug(
            'Creating config pod %s for %s',
            config_pod_name,
            server_deployment.metadata.name,
        )

        # ISSUE(https://github.com/reboot-dev/respect/issues/1430): Fix missing
        # ownership. Owner should be ServerDeployment, see above.
        config_pod_ip = await self._create_config_pod(
            namespace=application_namespace,
            pod_name=config_pod_name,
            container_name=CONFIG_CONTAINER_NAME,
            image=server_deployment.spec.container_image_name,
        )

        # TODO(benh): rework side-effect architecture of
        # 'OwnershipInformation' and make it side-effect free and
        # easier to reason about.
        server_config_ownership = OwnershipInformation.from_custom_object(
            server_deployment
        )

        server_config_metadata = kubernetes_asyncio.client.V1ObjectMeta(
            namespace=application_namespace,
            name=server_deployment.metadata.name,
        )

        # NOTE: `add_to_metadata()` mutates `server_config_metadata`!
        server_config_ownership.add_to_metadata(server_config_metadata)

        server_config = ServerConfig.from_proto(
            proto=await self._get_server_config(
                namespace=application_namespace,
                pod_name=config_pod_name,
                pod_ip=config_pod_ip,
            ),
            metadata=server_config_metadata,
        )

        # The ServerConfig we get back from the config pod is
        # incomplete.  Fill in the blanks.
        server_config.spec.server_deployment_name = server_deployment.metadata.name
        server_config.spec.container_image_name = server_deployment.spec.container_image_name

        await self._k8s_client.custom_objects.create_or_update(server_config)

        await self._k8s_client.pods.delete(
            application_namespace, config_pod_name
        )

        logger.debug(
            f'Deleted config pod {config_pod_name} for '
            f'{server_deployment.metadata.name}. Be aware, it may still be '
            ' in state `Terminating`.'
        )

    async def _create_config_pod(
        self,
        namespace: str,
        pod_name: str,
        container_name: str,
        image: str,
    ) -> RoutableAddress:
        """Create config pod and return the IP address of the config pod."""
        metadata = kubernetes_asyncio.client.V1ObjectMeta(
            namespace=namespace,
            name=pod_name,
        )

        pod = kubernetes_asyncio.client.V1Pod(
            metadata=metadata,
            spec={
                'serviceAccountName':
                    APPLICATION_SERVICE_ACCOUNT,
                'containers':
                    [
                        {
                            'name':
                                container_name,
                            'image':
                                image,
                            'imagePullPolicy':
                                'IfNotPresent',
                            'env':
                                [
                                    {
                                        'name': ENVVAR_RESEMBLE_MODE,
                                        'value': RESEMBLE_MODE_CONFIG
                                    },
                                    {
                                        'name':
                                            ENVVAR_RESEMBLE_CONFIG_SERVER_PORT,
                                        'value':
                                            f'{KUBERNETES_CONFIG_SERVER_PORT}'
                                    },
                                    # Ensure that any Python process
                                    # always produces their output
                                    # immediately. This is helpful for
                                    # debugging purposes.
                                    {
                                        'name': 'PYTHONUNBUFFERED',
                                        'value': '1'
                                    },
                                ],
                        }
                    ]
            }
        )

        logger.debug(
            'Creating config pod: (namespace=%s, pod_name=%s, container_name=%s, image=%s)',
            namespace, pod_name, container_name, image
        )

        # TODO: Consider making the ServerDeployment the owner of the Pod object
        # for added safety, in case the ServerDeployment is deleted while the
        # config pod is running.
        # ISSUE(https://github.com/reboot-dev/respect/issues/1430): Fix ownership.
        await self._k8s_client.pods.create(pod=pod)

        logger.debug('Waiting for config pod to come up...')
        try:
            await asyncio.wait_for(
                self._k8s_client.pods.wait_for_running(
                    namespace=namespace, name=pod_name
                ),
                timeout=self.CONFIG_POD_TIMEOUT_SECONDS,
            )
        except asyncio.exceptions.TimeoutError as e:
            raise InputError(
                reason='Timed out waiting for config pod to come up',
                parent_exception=e,
            ) from e

        pods = await self._k8s_client.pods.list_all(namespace=namespace)

        # Return first found ip-address if pod metadata name matches pod name,
        # if no ip address is found, raise an error.
        for ip_address in [
            pod.status.pod_ip for pod in pods if pod.metadata.name == pod_name
        ]:
            return ip_address

        raise InputError(reason='IP address not found for config-pod')

    async def _get_server_config(
        self,
        *,
        namespace: str,
        pod_name: str,
        pod_ip: RoutableAddress,
    ) -> server_config_pb2.ServerConfig:
        logger.info(f"Trying to get server config for '{namespace}'")

        async for retry in retry_insecure_grpc_unless_pods_have_failed(
            # This hardcoded server port KUBERNETES_CONFIG_SERVER_PORT
            # is safe because it will only ever run on Kubernetes
            # where there is no chance of a port conflict due to
            # simultaneous tests.
            f'{pod_ip}:{KUBERNETES_CONFIG_SERVER_PORT}',
            k8s_client=self._k8s_client,
            pods=[(namespace, [pod_name])],
            # TODO(benh): we only catch AioRpcError, but we should
            # also consider catching protobuf decoding errors.
            exceptions=[grpc.aio.AioRpcError],
        ):
            with retry() as channel:
                config_server_stub = config_mode_pb2_grpc.ConfigStub(channel)

                response = await config_server_stub.Get(
                    config_mode_pb2.GetConfigRequest()
                )

                return response.server_config
