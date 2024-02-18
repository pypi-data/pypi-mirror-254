import time
from resemble.controller.server_config import (
    ServerConfig,
    get_server_config_unique_name,
)
from resemble.v1alpha1 import placement_planner_pb2
from respect.logging import get_logger
from typing import Iterable, Optional

logger = get_logger(__name__)


class PlanMaker:
    """Logic to construct a placement Plan based on a set of currently valid
    ServerConfigs. Designed to be extendable for different Plan structures."""

    last_version: Optional[int] = None

    def make_plan(
        self, server_configs: Iterable[ServerConfig]
    ) -> placement_planner_pb2.Plan:
        """Construct a Plan for consensuses that will serve the given list of
        ServerConfigs."""
        service_plans = []
        # Map service names to their server names to make sure each service is
        # only served by one server.
        used_service_names: dict[str, str] = {}
        for server_config in server_configs:
            for service_name in server_config.spec.service_names:
                if service_name in used_service_names:
                    raise ValueError(
                        f'Service {service_name} registered under multiple '
                        f'servers: {used_service_names[service_name]} and '
                        f'{server_config.spec.server_deployment_name}'
                    )
                # We will use the same consensus for all services in a server.
                # NOTE: We should avoid appending anything to the name used to
                # avoid exceeding the maximum length of a kubernetes object.
                # NOTE(gorm,rjh) to future us: we had a suffix. This was bad.
                # Even when we'll have multiple consensuses, we'll need stable
                # names. One way of obtaining this could be to hash the server's
                # service names.
                consensus_name = server_config.spec.server_deployment_name

                # We only want one partition assignment for the whole keyspace
                # of the service.
                partition_assignment = placement_planner_pb2.PartitionAssignment(
                    partition=placement_planner_pb2.Partition(
                        first_key='', last_key=''
                    ),
                    consensus_name=consensus_name
                )
                service_plans.append(
                    placement_planner_pb2.ServicePlan(
                        service_name=service_name,
                        server_config_unique_name=get_server_config_unique_name(
                            server_config
                        ),
                        partition_assignments=[partition_assignment],
                    )
                )
                used_service_names[service_name
                                  ] = server_config.spec.server_deployment_name
        return placement_planner_pb2.Plan(
            version=self.get_version(), service_plans=service_plans
        )

    def get_version(self) -> int:
        """Return a valid version number that is (expected to be) greater than
        whatever was previously returned or used.
        We use a timestamp (in ns from epoch) to ensure that version numbers
        increase, and further verify that time has not somehow gone backwards.
        """
        timestamp = time.time_ns()
        if self.last_version is not None and timestamp <= self.last_version:
            raise RuntimeError(
                f'Time is not moving forward as expected! '
                f'New timestamp {timestamp} is not after '
                f'old timestamp {self.last_version}.'
            )
        self.last_version = timestamp
        return timestamp
