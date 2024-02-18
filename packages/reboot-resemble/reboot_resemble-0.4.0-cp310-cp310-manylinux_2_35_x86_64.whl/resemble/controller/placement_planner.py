import asyncio
import grpc
from concurrent import futures
from google.protobuf.descriptor_pb2 import FileDescriptorSet
from resemble.aio.types import ConsensusName
from resemble.controller.consensus_managers import ConsensusManager
from resemble.controller.exceptions import InputError
from resemble.controller.plan_makers import PlanMaker
from resemble.controller.server_config import ServerConfig
from resemble.controller.server_config_trackers import ServerConfigTracker
from resemble.v1alpha1 import placement_planner_pb2, placement_planner_pb2_grpc
from respect.logging import get_logger
from typing import AsyncGenerator, Awaitable, Callable, Optional

logger = get_logger(__name__)


class PlacementPlanner(placement_planner_pb2_grpc.PlacementPlannerServicer):

    def __init__(
        self, config_tracker: ServerConfigTracker,
        consensus_manager: ConsensusManager, address: str
    ) -> None:
        self.plan_maker = PlanMaker()
        self.config_tracker = config_tracker
        self.consensus_manager = consensus_manager
        # Use pubsub queues to be sure to notify all plan listeners whenever
        # there's a new plan.
        self.listener_queues: set[asyncio.Queue[
            placement_planner_pb2.PlanWithLocations]] = set()

        # Public set of callbacks that are called with the new PlanWithLocations
        # whenever one becomes available. Clients that want callbacks should add
        # their callbacks directly to this set.
        self.plan_change_callbacks: set[
            Callable[[placement_planner_pb2.PlanWithLocations],
                     Awaitable[None]]] = set()

        self._started = False

        self._server = grpc.aio.server(
            futures.ThreadPoolExecutor(max_workers=10)
        )

        placement_planner_pb2_grpc.add_PlacementPlannerServicer_to_server(
            self, self._server
        )

        self._port = self._server.add_insecure_port(address)
        self._host = address.split(':')[0]

        # Get notified when we need a new plan, either because the set of
        # ServerConfigs has changed or because consensuses have moved.
        async def make_plan_but_errors_are_input_errors() -> None:
            """Helper function to treat errors from `make_plan` as input errors.
            """
            try:
                await self.make_plan()
            except ValueError as e:
                raise InputError(
                    reason=str(e),
                    parent_exception=e,
                ) from e

        # Two conditions can cause a new plan to be made: either a location
        # change or a change to a `ServerConfig`. In case a new plan can not be
        # made, `make_plan` throws an exception, a `ValueError`. In case the
        # error stems from an change to a `ServerConfig`, this is an
        # `InputError` and should be propagated as such. To accomplish this we
        # use the helper function defined above as the callback in case of
        # `ServerConfig` changes.
        self.config_tracker.on_configs_change(
            make_plan_but_errors_are_input_errors
        )
        self.consensus_manager.on_locations_change(self.make_plan)

        self.current_plan_with_locations: Optional[
            placement_planner_pb2.PlanWithLocations] = None

    async def start(self) -> None:
        """Start a gRPC server at the given address to host the ListenForPlan
        endpoint."""
        await self.make_plan()
        await self._server.start()
        self._started = True
        logger.info(f"PlacementPlanner server started on port {self._port}")

    def port(self) -> int:
        return self._port

    def address(self) -> str:
        return f'{self._host}:{self._port}'

    async def stop(self) -> None:
        """Stop the gRPC server that was started.
        """
        if self._started:
            await self._server.stop(grace=None)
            logger.info('PlacementPlanner server stopped')

    async def make_plan(self) -> None:
        """Generate a new placement plan based on the currently valid set of
        ServerConfigs, update cluster resources to match the updated plan, and
        send the updated plan information out to all subscribed listeners."""
        server_configs: dict[
            str, ServerConfig] = await self.config_tracker.get_server_configs()
        logger.info(
            f'Making new plan based on {len(server_configs)} server configs: '
            f'{list(server_configs.keys())}'
        )

        new_plan = self.plan_maker.make_plan(server_configs.values())
        # Combine the Plan and the ServerConfigs into Consensuses.
        # Use a dict to implicitly de-duplicate so that each consensus name is
        # only included once.
        # ISSUE(https://github.com/reboot-dev/respect/issues/1452):
        # placement_planner_pb2.Consensus is only used internally. Replace with
        # a better data structure.
        consensuses: dict[ConsensusName, placement_planner_pb2.Consensus] = {}
        for service_plan in new_plan.service_plans:
            server_config = server_configs[
                service_plan.server_config_unique_name]

            for partition_assignment in service_plan.partition_assignments:
                file_descriptor_set = FileDescriptorSet()
                file_descriptor_set.ParseFromString(
                    server_config.spec.file_descriptor_set
                )
                consensuses[
                    partition_assignment.consensus_name
                ] = placement_planner_pb2.Consensus(
                    consensus_name=partition_assignment.consensus_name,
                    container_image_name=server_config.spec.
                    container_image_name,
                    k8s_namespace=server_config.metadata.namespace,
                    service_names=server_config.spec.service_names,
                    file_descriptor_set=file_descriptor_set,
                )
        logger.info(
            f'Plan version {new_plan.version} contains {len(consensuses)} consensuses'
        )
        logger.debug(
            f'Plan version {new_plan.version} consensuses: {consensuses.keys()}'
        )

        consensus_locations = await self.consensus_manager.set_consensuses(
            consensuses.values()
        )
        plan_with_locations = placement_planner_pb2.PlanWithLocations(
            plan=new_plan, locations=consensus_locations
        )
        self.current_plan_with_locations = plan_with_locations
        for queue in self.listener_queues:
            await queue.put(plan_with_locations)

        # Execute all callbacks for everyone.
        await asyncio.gather(
            *[
                callback(plan_with_locations)
                for callback in self.plan_change_callbacks
            ]
        )

        logger.info(f'Plan version {new_plan.version} active')

    async def ListenForPlan(
        self, request: placement_planner_pb2.ListenForPlanRequest, context
    ) -> AsyncGenerator[placement_planner_pb2.ListenForPlanResponse, None]:
        """Serve the current plan immediately, then send an update every time a
        new plan is generated."""
        queue: asyncio.Queue[placement_planner_pb2.PlanWithLocations
                            ] = asyncio.Queue()
        self.listener_queues.add(queue)

        if self.current_plan_with_locations is not None:
            # Clients should immediately get the current plan.
            await queue.put(self.current_plan_with_locations)

        while True:
            plan_with_locations = await queue.get()
            try:
                yield placement_planner_pb2.ListenForPlanResponse(
                    plan_with_locations=plan_with_locations
                )
            except GeneratorExit:
                # When the client disconnects, we will eventually get a
                # GeneratorExit thrown. We should clean up the state associated
                # with this client before returning.
                self.listener_queues.remove(queue)
                return
