import asyncio
import kubernetes_asyncio
import logging
from dataclasses import dataclass
from enum import Enum
from kubernetes_utils.kubernetes_client import (
    AbstractEnhancedKubernetesClient,
    EnhancedKubernetesClient,
)
from kubernetes_utils.resources.deployments import UpdateStrategy
from kubernetes_utils.resources.storage_classes import VolumeBindingMode
from resemble.controller.server_config import ServerConfig
from resemble.controller.server_deployment import ServerDeployment
from resemble.controller.settings import (
    APPLICATION_SERVICE_ACCOUNT,
    RESEMBLE_STORAGE_CLASS_NAME,
)
from typing import Optional

# Common parameters for our RBAC story.
CONTROLLER_SERVICE_ACCOUNT = 'resemble-controller'
DEPLOYER_SERVICE_ACCOUNT = 'single-resemble-deployer'

ISTIO_NAMESPACE_LABELS = {
    # Required to be set in order for Istio to inject sidecars into a Resemble
    # namespace.
    'istio-injection': 'enabled',
}


class StorageProvisioner(Enum):
    RANCHER_LOCAL_PATH = 'rancher.io/local-path'
    AWS_EBS = 'ebs.csi.aws.com'


@dataclass(kw_only=True)
class Config:
    # Kubernetes namespace names.
    system_namespace: str
    deployer_namespace: str
    application_namespaces: list[str]

    install_controller: bool
    # Required if `install_controller=True`.
    controller_image: Optional[str] = None

    # How will we provision storage?
    storage_provisioner: StorageProvisioner


async def _apply_rbac(
    k8s_client: AbstractEnhancedKubernetesClient, system_namespace: str,
    deployer_namespace: str, application_namespaces: list[str]
) -> None:
    """Ensure namespaces and role based access control."""

    # Ensure namespace and service account for resemble system.
    await k8s_client.namespaces.ensure_created(
        name=system_namespace, labels=ISTIO_NAMESPACE_LABELS
    )
    await k8s_client.service_accounts.ensure_created(
        namespace=system_namespace,
        name=CONTROLLER_SERVICE_ACCOUNT,
    )

    # Ensure namespace and service account for deployer.
    await k8s_client.namespaces.ensure_created(
        name=deployer_namespace, labels=ISTIO_NAMESPACE_LABELS
    )
    await k8s_client.service_accounts.ensure_created(
        namespace=deployer_namespace,
        name=DEPLOYER_SERVICE_ACCOUNT,
    )

    # Ensure role and role binding for controller.
    await k8s_client.cluster_roles.create_or_update(
        name='resemble-controller-role',
        rules=[
            kubernetes_asyncio.client.V1PolicyRule(
                api_groups=['reboot.dev'],
                resources=['serverdeployments'],
                verbs=[
                    'create',  # Used to bring up Consensuses for user containers on demand.
                    'update',  # Used to replace existing Consensuses whose details have changed.
                    'get',  # Used to fetch existing info needed when updating Consensuses.
                    'watch',  # Used to initiate Config Mode Pods.
                ],
            ),
            kubernetes_asyncio.client.V1PolicyRule(
                api_groups=['reboot.dev'],
                resources=['serverconfigs'],
                verbs=[
                    'watch',  # Used to track config creation and know when to make new plans.
                    'list',  # Used to fetch current list of ServerConfigs for plan-making.
                    'get',  # Used as part of our create_or_update.
                    'create',  # Used by the config extractor to create a ServerConfig.
                    'update',  # Used by the config extractor to update a ServerConfig.
                ],
            ),
            kubernetes_asyncio.client.V1PolicyRule(
                api_groups=['', 'apps'],
                resources=['deployments', 'services', 'pods', 'pods/log'],
                verbs=[
                    'create',  # Used to bring up Consensuses for user containers on demand.
                    'update',  # Used to replace existing Consensuses whose details have changed.
                    'get',  # Used to fetch existing info needed when updating Consensuses, and logs.
                    'list',  # Used to list Pods, needed to address config pod.
                    'watch',  # Also used to list Pods, needed to address config pod, and follow logs.
                    'delete',  # Used to delete config pod.
                ],
            ),
            kubernetes_asyncio.client.V1PolicyRule(
                api_groups=['networking.istio.io'],
                resources=['virtualservices'],
                verbs=[
                    'create',  # Used to create the Resemble VirtualService.
                    'update',  # Used to update the Resemble VirtualService.
                    'get',  # Used to hermetically update the Resemble VirtualService.
                    'delete',  # Used to delete the Resemble VirtualService when it's no longer needed.
                ],
            ),
            kubernetes_asyncio.client.V1PolicyRule(
                api_groups=['networking.istio.io'],
                resources=['envoyfilters'],
                verbs=[
                    'create',  # Used to create the Resemble routing filter.
                    'update',  # Used to update the Resemble routing filter.
                    'get',  # Used to hermetically update the Resemble routing filter.
                    'list',  # Used to get unused filters.
                    'delete',  # Used to delete unused filters.
                ],
            ),
            kubernetes_asyncio.client.V1PolicyRule(
                api_groups=['networking.istio.io'],
                resources=['gateways'],
                verbs=[
                    'create',  # Used to create the Resemble Gateway.
                    'update',  # Used to update the Resemble Gateway.
                    'get',  # Used to hermetically update the Resemble Gateway.
                ],
            ),
            kubernetes_asyncio.client.V1PolicyRule(
                api_groups=[''],
                resources=['persistentvolumeclaims'],
                verbs=[
                    'create',  # Used to create persistent volume claims for apps.
                    'update',  # Used to update persistent volume claims for apps.
                    'get',  # Used to hermetically update persistent volume claims.
                    'delete',  # Used to delete persistent volume claims when they're no longer needed.
                ],
            ),
        ],
    )

    await k8s_client.cluster_role_bindings.create_or_update(
        name='resemble-controller-binding',
        role_name='resemble-controller-role',
        subjects=[
            kubernetes_asyncio.client.V1Subject(
                kind='ServiceAccount',
                namespace=system_namespace,
                name=CONTROLLER_SERVICE_ACCOUNT,
            ),
        ],
    )

    for application_namespace in application_namespaces:
        # Each application namespace gets its own application service account.
        await k8s_client.namespaces.ensure_created(
            name=application_namespace, labels=ISTIO_NAMESPACE_LABELS
        )
        await k8s_client.service_accounts.ensure_created(
            namespace=application_namespace,
            name=APPLICATION_SERVICE_ACCOUNT,
        )

        # Ensure role and role binding, allowing the resemble deployer to create a
        # ServerDeployment object in each application namespace.
        await k8s_client.roles.create_or_update(
            namespace=application_namespace,
            name='resemble-deployer-role',
            rules=[
                kubernetes_asyncio.client.V1PolicyRule(
                    api_groups=['reboot.dev'],
                    resources=['serverdeployments'],
                    verbs=[
                        'create',  # To create a server deployment.
                        'delete',  # To delete a server deployment.
                    ],
                )
            ],
        )

        await k8s_client.role_bindings.create_or_update(
            namespace=application_namespace,
            name='resemble-deployer-binding',
            role_name='resemble-deployer-role',
            subjects=[
                # Lists every deployer that can deploy to this app.
                # For M1, that’s only the one deployer account.
                kubernetes_asyncio.client.V1Subject(
                    kind='ServiceAccount',
                    namespace=deployer_namespace,
                    name=DEPLOYER_SERVICE_ACCOUNT,
                ),
            ],
        )


async def _teardown_namespaces(
    k8s_client: AbstractEnhancedKubernetesClient, system_namespace: str,
    deployer_namespace: str, application_namespaces: list[str]
):
    """Clean up our Resemble installation.

    The simplest approach here is to delete the namespaces and be done with it,
    so that's what we do. We don't wait for cleanup to complete before
    returning, as that has been shown to cause a ~30 second slowdown in the
    termination of tests using this method.
    """
    return_values = await asyncio.gather(
        k8s_client.namespaces.delete(name=system_namespace),
        k8s_client.namespaces.delete(name=deployer_namespace),
        *[
            k8s_client.namespaces.delete(name=application_namespace)
            for application_namespace in application_namespaces
        ],
        # Don't let exceptions propagate.
        return_exceptions=True
    )

    # Emit log messages if an exception was incurred.
    exceptions = [v for v in return_values if isinstance(v, Exception)]
    if len(exceptions) > 0:
        # TODO: Use resemble logging when we has it.
        logging.fatal(
            'Got the following exceptions while removing namespaces: %s',
            exceptions
        )


async def _install_storage(
    k8s_client: AbstractEnhancedKubernetesClient,
    provisioner: StorageProvisioner,
) -> None:
    await k8s_client.storage_classes.create_or_update(
        name=RESEMBLE_STORAGE_CLASS_NAME,
        provisioner=provisioner.value,
        volume_binding_mode=VolumeBindingMode.WAIT_FOR_FIRST_CONSUMER,
        allow_volume_expansion=True,
    )


async def _uninstall_storage(k8s_client: AbstractEnhancedKubernetesClient):
    await k8s_client.storage_classes.delete(name=RESEMBLE_STORAGE_CLASS_NAME)


async def _install_controller(
    k8s_client: AbstractEnhancedKubernetesClient,
    controller_image: str,
    system_namespace: str,
) -> None:

    env = [
        kubernetes_asyncio.client.V1EnvVar(
            name='KUBERNETES_POD_NAMESPACE',
            value_from=kubernetes_asyncio.client.V1EnvVarSource(
                field_ref=kubernetes_asyncio.client.V1ObjectFieldSelector(
                    api_version='v1',
                    field_path='metadata.namespace',
                ),
            ),
        ),
        kubernetes_asyncio.client.V1EnvVar(
            name='KUBERNETES_POD_NAME',
            value_from=kubernetes_asyncio.client.V1EnvVarSource(
                field_ref=kubernetes_asyncio.client.V1ObjectFieldSelector(
                    api_version='v1',
                    field_path='metadata.name',
                ),
            ),
        ),
        kubernetes_asyncio.client.V1EnvVar(
            name='KUBERNETES_POD_UID',
            value_from=kubernetes_asyncio.client.V1EnvVarSource(
                field_ref=kubernetes_asyncio.client.V1ObjectFieldSelector(
                    api_version='v1',
                    field_path='metadata.uid',
                ),
            ),
        ),
    ]

    await k8s_client.deployments.create_or_update(
        namespace=system_namespace,
        deployment_name='resemble-controller',
        container_image_name=controller_image,
        replicas=1,
        # During an update, remove any previous controller before starting a new
        # one. That avoids having multiple controllers thinking they're in
        # charge - at the expense of a brief period where there is no
        # controller.
        #
        # The temporary period without a running controller does not affect the
        # users applications other than potentially introducing a small delay
        # before new deployment updates are made. This scenario is equivalent to
        # if the resemble controller had crashed for other reasons.
        update_strategy=UpdateStrategy.RECREATE,
        env=env,
        service_account_name=CONTROLLER_SERVICE_ACCOUNT,
    )

    await k8s_client.deployments.wait_for_started(
        namespace=system_namespace, name='resemble-controller'
    )


async def _ensure_custom_resource_definitions(
    k8s_client: AbstractEnhancedKubernetesClient
) -> None:
    """Install resemble custom resource definitions."""
    await k8s_client.custom_resource_definitions.create(ServerDeployment)
    await k8s_client.custom_resource_definitions.create(ServerConfig)


async def _delete_custom_resource_definitions(
    k8s_client: AbstractEnhancedKubernetesClient
) -> None:
    """Remove resemble custom resource definitions."""
    await k8s_client.custom_resource_definitions.ensure_deleted(
        ServerDeployment
    )
    await k8s_client.custom_resource_definitions.ensure_deleted(ServerConfig)


@dataclass(kw_only=True)
class Installation:
    """Represents a running cluster, with enough information about its config
    that it can tear the cluster down when requested. Constructed by setting
    up an installation using `setup()`."""
    config: Config

    @staticmethod
    async def setup_with_kubeconfig(
        config: Config, *, kubeconfig: str
    ) -> 'Installation':
        """Install Resemble in the currently active Kubernetes cluster."""
        k8s_client = await EnhancedKubernetesClient.create_client_from_kubeconfig(
            kubeconfig
        )
        try:
            return await Installation.setup_with_client(
                config, k8s_client=k8s_client
            )
        finally:
            # The way we are using the underlying kubernetes client, we never
            # automatically close the network connection and thus we must do this
            # manually.
            await k8s_client.close()

    @staticmethod
    async def setup_with_context(
        config: Config, *, context: str
    ) -> 'Installation':
        """Install Resemble in the currently active Kubernetes cluster."""
        k8s_client = await EnhancedKubernetesClient.create_client(context)
        try:
            return await Installation.setup_with_client(
                config, k8s_client=k8s_client
            )
        finally:
            # The way we are using the underlying kubernetes client, we never
            # automatically close the network connection and thus we must do this
            # manually.
            await k8s_client.close()

    @staticmethod
    async def setup_with_client(
        config: Config, *, k8s_client: AbstractEnhancedKubernetesClient
    ) -> 'Installation':
        """
        Set up a Resemble installation in the cluster connected to the given
        `k8s_client`.

        Does not take ownership of `k8s_client`; the caller must close that
        client when they're done with it.
        """
        await _ensure_custom_resource_definitions(k8s_client)

        await _apply_rbac(
            k8s_client,
            config.system_namespace,
            config.deployer_namespace,
            config.application_namespaces,
        )

        await _install_storage(
            k8s_client,
            config.storage_provisioner,
        )

        if config.install_controller:
            if config.controller_image is None:
                raise ValueError(
                    "Must specify `ClusterConfig.controller_image` "
                    "if `ClusterConfig.install_controller=True`"
                )
            await _install_controller(
                k8s_client,
                config.controller_image,
                config.system_namespace,
            )

        return Installation(config=config)

    async def teardown_with_kubeconfig(self, kubeconfig: str) -> None:
        """Remove resemble cluster modifications."""
        k8s_client = await EnhancedKubernetesClient.create_client_from_kubeconfig(
            kubeconfig
        )
        try:
            return await self.teardown_with_client(k8s_client)
        finally:
            # The way we are using the underlying kubernetes client, we never
            # automatically close the network connection and thus we must do this
            # manually.
            await k8s_client.close()

    async def teardown_with_context(self, context: str) -> None:
        """Remove resemble cluster modifications."""
        k8s_client = await EnhancedKubernetesClient.create_client(context)
        try:
            return await self.teardown_with_client(k8s_client)
        finally:
            # The way we are using the underlying kubernetes client, we never
            # automatically close the network connection and thus we must do this
            # manually.
            await k8s_client.close()

    async def teardown_with_client(
        self, k8s_client: AbstractEnhancedKubernetesClient
    ) -> None:
        await _delete_custom_resource_definitions(k8s_client)

        await _teardown_namespaces(
            k8s_client,
            self.config.system_namespace,
            self.config.deployer_namespace,
            self.config.application_namespaces,
        )

        await _uninstall_storage(k8s_client)
