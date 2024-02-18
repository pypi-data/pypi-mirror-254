import asyncio
import kubernetes_asyncio
from aiohttp.client_exceptions import ClientConnectorError
from respect.logging import LoggerMixin
from typing import Awaitable, Callable, TypeVar

RetryReturnT = TypeVar('RetryReturnT')


class KubernetesAPIs(LoggerMixin):

    def __init__(self, k8s_config_initialized: bool = False):
        if not k8s_config_initialized:
            raise ValueError(
                'K8s API config must be loaded before calling this constructor.'
                ' Use EnhancedKubernetesClient.create_client() rather than'
                ' calling this constructor directly.'
            )
        super().__init__()

        self._client = kubernetes_asyncio.client.ApiClient()
        self.rbac_authz = kubernetes_asyncio.client.RbacAuthorizationV1Api(
            self._client
        )
        self.core = kubernetes_asyncio.client.CoreV1Api(self._client)
        self.custom_objects = kubernetes_asyncio.client.CustomObjectsApi(
            self._client
        )
        self.apps = kubernetes_asyncio.client.AppsV1Api(self._client)
        self.api_extensions = kubernetes_asyncio.client.ApiextensionsV1Api(
            self._client
        )
        self.storage = kubernetes_asyncio.client.StorageV1Api(self._client)

    async def close(self) -> None:
        """Close client connection(s)."""
        await self._client.close()

    async def retry_api_call(
        self,
        fn: Callable[[], Awaitable[RetryReturnT]],
        num_attempts: int = 60,
        sleep_length_seconds: float = 2,
        retry_api_exception: bool = False
    ) -> RetryReturnT:
        """Retries a k8s API call a few times in case of transient errors.
        These errors are likely to happen when a pod is first starting up -
        its Istio proxy may not yet be ready to handle traffic."""
        for _ in range(num_attempts):
            try:
                return await fn()
            except ClientConnectorError as e:
                # This likely indicates the Kubernetes API server isn't
                # reachable (yet); that's a common transient condition in our
                # tests just after they've started, even when the API server has
                # been up for a while - the exact cause is unclear.
                # TODO(rjh): figure out why the API frequently isn't available
                # at the start of a test; is there anything we can do to wait
                # until the API is available?
                self.logger.warning(
                    f'Got an exception calling Kubernetes: {e}'
                )
                # Give the API a chance to come up.
                self.logger.warning(
                    f'Retrying after {sleep_length_seconds} seconds...'
                )
                await asyncio.sleep(sleep_length_seconds)
            except kubernetes_asyncio.client.exceptions.ApiException as e:
                # The API is reachable, but had a (possibly transient) error.
                # For example, we've observed this for conflicts when labeling
                # nodes, where some other process modified the node at the same
                # time as us, and the API server rejected our (now stale)
                # request. Some operations will want to retry this, while others
                # will want to handle it themselves.
                if retry_api_exception:
                    self.logger.warning(
                        f'Got an API exception calling Kubernetes: {e}'
                    )
                    self.logger.warning('Retrying immediately...')
                else:
                    raise e

        raise TimeoutError(
            'Failed to perform operation; maximum retries exceeded.'
        )
