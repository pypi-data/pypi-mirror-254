from kubernetes_utils.kubernetes_client import AbstractEnhancedKubernetesClient
from resemble.controller.exceptions import InputError
from resemble.controller.server_config import (
    ServerConfig,
    get_server_config_unique_name,
)
from respect.logging import get_logger
from typing import Awaitable, Callable

logger = get_logger(__name__)


class ServerConfigTracker:

    def __init__(self):
        # All callbacks registered with this tracker, to be called on any
        # ServerConfig event.
        self.config_change_callbacks: list[Callable[[], Awaitable[None]]] = []

    async def get_server_configs(self) -> dict[str, ServerConfig]:
        """Return a map of server name to ServerConfig."""
        raise NotImplementedError()

    def on_configs_change(self, callback: Callable[[], Awaitable[None]]):
        """Store a callback function to invoke whenever a server config is
        added, updated, or deleted.
        We expect our callbacks to be async functions with no params."""
        self.config_change_callbacks.append(callback)


class KubernetesServerConfigTracker(ServerConfigTracker):

    def __init__(
        self,
        k8s_client: AbstractEnhancedKubernetesClient,
    ):
        super().__init__()
        self._k8s_client = k8s_client

    async def run(self) -> None:
        """Start tracking ServerConfig events.
        Note that this function is expected to run indefinitely."""
        await self._watch_server_config()

    async def _watch_server_config(self) -> None:
        """Start a watch on the ServerConfig definition with the k8s API, and
        call all our callbacks on any event."""
        logger.info('Starting ServerConfig watch in any namespace...')
        async for watch_event in self._k8s_client.custom_objects.watch_all(
            object_type=ServerConfig,
        ):
            logger.info(
                'ServerConfig %s: %s',
                watch_event.type,
                watch_event.object.metadata.name or 'unknown',
            )
            try:
                for callback in self.config_change_callbacks:
                    await callback()
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

        logger.info('Stopped watching for ServerConfig changes')

    async def get_server_configs(self) -> dict[str, ServerConfig]:
        server_config_dict: dict[str, ServerConfig] = {}
        server_configs = await self._k8s_client.custom_objects.list_all(
            object_type=ServerConfig,
        )
        for server_config in server_configs:
            if (
                len(server_config.spec.server_deployment_name) == 0 or
                len(server_config.spec.file_descriptor_set) == 0 or
                len(server_config.spec.container_image_name) == 0 or
                len(server_config.spec.service_names) == 0
            ):
                # ISSUE(https://github.com/reboot-dev/respect/issues/1416):
                # Controller should handle incorrect user input. We should
                # propagate this message back to the user instead of silently
                # failing.
                logger.warning(
                    'ServerConfig %s in %s is missing required fields, skipping',
                    server_config.metadata.name,
                    server_config.metadata.namespace,
                )
                continue

            server_config_dict[get_server_config_unique_name(server_config)
                              ] = server_config

        return server_config_dict


class LocalServerConfigTracker(ServerConfigTracker):

    def __init__(self):
        super().__init__()
        # Mapping of server name to full ServerConfig.
        self.configs: dict[str, ServerConfig] = {}

    async def add_config(self, config: ServerConfig) -> None:
        self.configs[get_server_config_unique_name(config)] = config
        for callback in self.config_change_callbacks:
            await callback()

    async def delete_config(self, config: ServerConfig) -> None:
        self.configs.pop(get_server_config_unique_name(config), None)
        for callback in self.config_change_callbacks:
            await callback()

    async def delete_all_configs(self) -> None:
        self.configs = {}
        for callback in self.config_change_callbacks:
            await callback()

    async def get_server_configs(self) -> dict[str, ServerConfig]:
        return self.configs
