import multiprocessing
import os
import threading
from resemble.aio.auth.token_verifiers import TokenVerifier
from resemble.aio.errors import Error, UnknownService
from resemble.aio.internals.channel_manager import _ChannelManager
from resemble.aio.once import Once
from resemble.aio.resolvers import DirectResolver
from resemble.aio.servicers import Serviceable, Servicer
from resemble.aio.types import (
    ActorId,
    ConsensusName,
    RoutableAddress,
    ServiceName,
)
from resemble.aio.workflows import Workflow
from resemble.controller.config_extractor import LocalConfigExtractor
from resemble.controller.consensus_managers import LocalConsensusManager
from resemble.controller.placement_planner import PlacementPlanner
from resemble.controller.server_config import (
    ServerConfig,
    get_server_config_unique_name,
)
from resemble.controller.server_config_trackers import LocalServerConfigTracker
from resemble.v1alpha1 import placement_planner_pb2
from respect.logging import ERROR, get_logger, set_log_level
from typing import Optional

logger = get_logger(__name__)


def _initialize_multiprocessing_start_method():
    # We don't want any threads to be running when we try and spawn
    # the forkserver via `multiprocessing.set_start_method()`, but we
    # make an exception (for now) when we're getting called through
    # from nodejs as those threads *must* be created in order to call
    # into us in the first place.
    #
    # See 'resemble/nodejs/python.py'.
    if threading.active_count() > 1 and os.environ.get(
        'RESEMBLE_NODEJS_EVENT_LOOP_THREAD',
        'false',
    ).lower() != 'true':
        raise RuntimeError(
            'Resemble must be initialized before creating any threads'
        )

    multiprocessing_start_method = multiprocessing.get_start_method(
        allow_none=True
    )

    if multiprocessing_start_method is None:
        # We want to use 'forkserver', which should be set before any
        # threads are created, so that users _can_ use threads in
        # their tests and we will be able to reliably fork without
        # worrying about any gotchas due to forking a multi-threaded
        # process.
        multiprocessing.set_start_method('forkserver')
    elif multiprocessing_start_method != 'forkserver':
        raise RuntimeError(
            f"Resemble requires the 'forkserver' start method but you "
            f"appear to have configured '{multiprocessing_start_method}'"
        )


# We're using a global here because we only want to initialize the
# multiprocessing start method once per process.
_initialize_multiprocessing_start_method_once = Once(
    _initialize_multiprocessing_start_method
)


class Resemble:

    def __init__(self):
        global _initialize_multiprocessing_start_method_once

        _initialize_multiprocessing_start_method_once()

        # TODO(rjh, benh): set up a logging system that allows us to increase
        # the verbosity level of the logs by environment variable.
        #
        # See also: matching line in
        #   `resemble.aio.applications.Application.__init__`.
        set_log_level(ERROR)

        self._running_service_names: set[str] = set()
        self._consensus_manager = LocalConsensusManager()
        self._config_tracker = LocalServerConfigTracker()
        self._config_extractor = LocalConfigExtractor()

        self._consensuses_by_name: dict[ConsensusName,
                                        placement_planner_pb2.Consensus] = {}

        self._placement_planner = PlacementPlanner(
            self._config_tracker,
            self._consensus_manager,
            # Let the PlacementPlanner choose its own port locally, in
            # case we are running multiple PlacementPlanners on the
            # same host (for example, running multiple unit tests in
            # parallel).
            '127.0.0.1:0'
        )

        self._consensus_manager.register_placement_planner_address(
            self._placement_planner.address()
        )

        self._resolver = DirectResolver(self._placement_planner.address())
        self._channel_manager = _ChannelManager(
            self._resolver,
            # Not using a secure channel, since this will all be localhost
            # traffic that does not flow through the gateway, which is the
            # only place we do `localhost.direct` SSL termination.
            secure=False,
        )

    async def start(self):
        await self._placement_planner.start()
        await self._resolver.start()

    def create_workflow(
        self,
        *,
        name: str,
        bearer_token: Optional[str] = None,
    ) -> Workflow:
        """ Create a Workflow for use in tests.
        """
        return Workflow(
            name=name,
            channel_manager=self._channel_manager,
            bearer_token=bearer_token,
        )

    async def up(
        self,
        *,
        servicers: Optional[list[type[Servicer]]] = None,
        # A legacy gRPC servicer type can't be more specific than `type`,
        # because legacy gRPC servicers (as generated by the gRPC `protoc`
        # plugin) do not share any common base class other than `object`.
        legacy_grpc_servicers: Optional[list[type]] = None,
        token_verifier: Optional[TokenVerifier] = None,
        config: Optional[ServerConfig] = None,
        in_process: bool = False,
        local_envoy: bool = False,
        local_envoy_port: int = 0,
        name: Optional[str] = None,
        directory: Optional[str] = None,
    ) -> ServerConfig:
        """ Bring up a collection of servicers, or an already brought up
        instance identifiable via its ServerConfig.

        in_process: If False, bring up Resemble in a separate process - to
        prevent user-facing log spam from gRPC. gRPC has an issue
        [#25364](https://github.com/grpc/grpc/issues/25364), open since Feb
        2021, that logs errant BlockingIOErrors if gRPC is in a multi-process
        Python context. If True, servicers are brought up in the current
        process and users will have to know to just ignore BlockingIOErrors.

        local_envoy: If True, bring up a LocalEnvoy proxy for our Resemble
        services.

        local_envoy_port: port on which to connect to Envoy,
        defaults to 0 (picked dynamically by the OS).

        name: name to use to override the default (randomly generated)
        deployment name.

        directory: directory in which to have the sidecar store its
        state.
        """
        if servicers is None and legacy_grpc_servicers is None and config is None:
            raise ValueError(
                "One of 'servicers', 'legacy_grpc_servicers', or 'config' must "
                "be passed"
            )

        if config is not None:
            if servicers is not None or legacy_grpc_servicers is not None:
                raise ValueError(
                    "Only pass one of ('servicers' and/or 'legacy_grpc_servicers') "
                    "or 'config'"
                )
            elif name is not None:
                raise ValueError(
                    "Passing 'name' is not valid when passing 'config'"
                )
            elif directory is not None:
                raise ValueError(
                    "Passing 'directory' is not valid when passing 'config'"
                )

            # Is there already a consensus running with the name associated with
            # this config? Updating a running config is not allowed.
            running_configs = await self._config_tracker.get_server_configs()
            config_unique_name = get_server_config_unique_name(config)
            if config_unique_name in running_configs:
                raise ValueError(
                    f'Config {config_unique_name} is already running. '
                    f'Updating a running config in dev mode is not allowed'
                )

            # This is a new config. We just need to check that it doesn't
            # conflict with any servicers already running.
            for service_name in config.spec.service_names:
                if service_name in self._running_service_names:
                    raise ValueError(
                        f"A servicer for '{service_name}' "
                        "has already been brought up"
                    )

        serviceables: list[Serviceable] = []
        for servicer in servicers or []:
            serviceables.append(Serviceable.from_servicer_type(servicer))
        for legacy_grpc_servicer in legacy_grpc_servicers or []:
            serviceables.append(
                Serviceable.from_servicer_type(legacy_grpc_servicer)
            )
        # To prevent typos mixing up `servicers` and `serviceables`, delete
        # `servicers` (so that mypy can catch if we accidentally use it).
        del servicers

        if len(serviceables) > 0:
            for serviceable in serviceables:
                if serviceable.service_name() in self._running_service_names:
                    raise ValueError(
                        f"A servicer for '{serviceable.service_name()}' "
                        "has already been brought up"
                    )

            self._consensus_manager.register_serviceables(
                serviceables=serviceables,
                token_verifier=token_verifier,
                in_process=in_process,
                local_envoy=local_envoy,
                local_envoy_port=local_envoy_port,
                directory=directory,
            )

            config = self._config_extractor.config_from_serviceables(
                serviceables
            )

            if name is not None:
                config.spec.server_deployment_name = name

        assert config is not None

        # This addition will trigger a new plan being made.
        await self._config_tracker.add_config(config)

        # Yield the event loop and wait for the DirectResolver to pick
        # up the new plan.
        await self._resolver.wait_for_service_names(config.spec.service_names)

        self._running_service_names.update(config.spec.service_names)
        return config

    def https_localhost_direct_uri(
        self,
        # A legacy gRPC servicer type can't be more specific than `type`,
        # because legacy gRPC servicers (as generated by the gRPC `protoc`
        # plugin) do not share any common base class other than `object`.
        servicer: type[Servicer] | type,
        path: str = '',
    ):
        return f"https://{self.localhost_direct_endpoint(servicer, path)}"

    def localhost_direct_endpoint(
        self,
        # A legacy gRPC servicer type can't be more specific than `type`,
        # because legacy gRPC servicers (as generated by the gRPC `protoc`
        # plugin) do not share any common base class other than `object`.
        servicer: type[Servicer] | type,
        path: str = '',
    ):
        """Returns the Envoy proxy endpoint."""
        serviceable = Serviceable.from_servicer_type(servicer)

        if serviceable.service_name() not in self._running_service_names:
            raise ValueError(f'Servicer {servicer} has not been brought up')

        envoy = self._consensus_manager.get_local_envoy_for_serviceable(
            serviceable
        )

        if envoy is None:
            raise ValueError(
                f"No local Envoy was launched for servicer {servicer}; "
                "did you forget to pass 'local_envoy=True'?"
            )

        return f'localhost.direct:{envoy.port}{path}'

    def resolve(
        self, servicer: type[Servicer], actor_id: ActorId
    ) -> RoutableAddress:
        """Return the RoutableAddress for a given Servicer type and ActorId.
        """
        address: Optional[RoutableAddress] = self._resolver.resolve(
            servicer, actor_id
        )

        if address is None:
            logger.error(
                f"Servicer for service '{servicer.__service_name__}' "
                "has not been brought up"
            )
            raise Error(UnknownService())

        return address

    async def stop(self) -> None:
        """Bring down all servicers and shut down the Resemble instance such
        that no more servicers can be brought up. """
        try:
            await self.down()
        finally:
            try:
                await self._resolver.stop()
            finally:
                await self._placement_planner.stop()

    async def down(self, config: Optional[ServerConfig] = None) -> None:
        """Bring down either a single config or everything that has been
        brought up.
        """
        if config is None:
            # Delete all configs so that the PlacementPlanner will bring
            # down all consensuses.
            await self._config_tracker.delete_all_configs()
            self._running_service_names = set()

            # TODO(benh): actually wait for everything to be down by
            # awaiting the resolver to have a new plan (with 0
            # consensuses)?
        else:
            # Get addresses the resolver currently knows about.
            addresses: dict[ServiceName,
                            RoutableAddress] = self._resolver.addresses()

            for service_name in config.spec.service_names:
                # Remove all the services we expect to be brought down.
                del addresses[service_name]

                # Proactively remove each service name so that while we
                # wait for the config to be deleted and the resolver
                # to get the updated plan any concurrent calls into
                # this instance will raise.
                self._running_service_names.remove(service_name)

            await self._config_tracker.delete_config(config)

            # Now wait for the resolver to see that all of those
            # services are no longer part of the plan.
            await self._resolver.wait_for_expected(addresses)
