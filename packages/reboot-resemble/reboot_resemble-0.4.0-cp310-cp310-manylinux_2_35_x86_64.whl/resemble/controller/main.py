from __future__ import annotations

import asyncio
import kubernetes_asyncio
import os
import respect.logging as logging
from kubernetes_utils.kubernetes_client import EnhancedKubernetesClient
from resemble.controller.config_extractor import KubernetesConfigExtractor
from resemble.controller.consensus_managers import KubernetesConsensusManager
from resemble.controller.network_managers import KubernetesNetworkManager
from resemble.controller.placement_planner import PlacementPlanner
from resemble.controller.server_config_trackers import (
    KubernetesServerConfigTracker,
)

logger = logging.get_logger(__name__)


async def main():
    # TODO(rjh): remove this once the controller is ready to run in production,
    #            so the log level goes back to default (INFO).
    logging.set_log_level(logging.DEBUG)
    own_pod_namespace = os.environ.get('KUBERNETES_POD_NAMESPACE')
    own_pod_name = os.environ.get('KUBERNETES_POD_NAME')
    own_pod_uid = os.environ.get('KUBERNETES_POD_UID')
    if own_pod_namespace is None or own_pod_name is None or own_pod_uid is None:
        raise ValueError(
            f'Missing required Kubernetes downward API environment variables: '
            f'namespace={own_pod_namespace}, name={own_pod_name}, uid={own_pod_uid}'
        )
    own_pod_metadata = kubernetes_asyncio.client.V1ObjectMeta(
        namespace=own_pod_namespace, name=own_pod_name, uid=own_pod_uid
    )

    # We're on Kubernetes, so create an incluster client.
    k8s_client = await EnhancedKubernetesClient.create_incluster_client()
    consensus_manager = KubernetesConsensusManager(
        system_namespace=own_pod_namespace, k8s_client=k8s_client
    )
    server_config_tracker = KubernetesServerConfigTracker(k8s_client)
    config_extractor = KubernetesConfigExtractor(k8s_client)
    placement_planner = PlacementPlanner(
        server_config_tracker, consensus_manager, '0.0.0.0:0'
    )
    # ATTENTION, after `start()`ing it we MUST `stop()` the `PlacementPlanner`
    # even if the program crashes, otherwise the `PlacementPlanner` will keep
    # running in the background and prevent the program from exiting.
    await placement_planner.start()

    try:
        network_manager = KubernetesNetworkManager(
            k8s_client, placement_planner, own_pod_metadata
        )

        # To be sure that we eventually await all the necessary tasks for the
        # different controller components, we collect them into a single future
        # using `asyncio.gather()`.
        # Note: if either of these tasks raises, we expect the exception to crash
        # the program, thus we don't bother to gently cancel the other task.
        await asyncio.gather(
            server_config_tracker.run(),
            config_extractor.run(),
            network_manager.run(),
        )
    finally:
        # As mentioned above, we MUST stop the `PlacementPlanner`, even when
        # crashing.
        await placement_planner.stop()


if __name__ == '__main__':
    asyncio.run(main())
    logger.info('Done with main function')
