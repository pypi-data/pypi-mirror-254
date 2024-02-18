import asyncio
import kubernetes_asyncio
import resemble.v1alpha1.istio.gateway_spec_pb2 as gateway_spec_pb2
from kubernetes_utils.kubernetes_client import AbstractEnhancedKubernetesClient
from kubernetes_utils.ownership import OwnershipInformation
from resemble.aio.headers import CONSENSUS_ID_HEADER
from resemble.aio.types import ConsensusName, KubernetesNamespace, ServiceName
from resemble.controller.envoy_filter import EnvoyFilter
from resemble.controller.envoy_filter_generator import (
    FilterContext,
    generate_istio_routing_filter,
)
from resemble.controller.gateway import Gateway, GatewaySpec
from resemble.controller.placement_planner import PlacementPlanner
from resemble.controller.settings import (
    ISTIO_ALL_SIDECARS_GATEWAY_NAME,
    ISTIO_INGRESSGATEWAY_INTERNAL_PORT,
    ISTIO_INGRESSGATEWAY_LABEL_NAME,
    ISTIO_INGRESSGATEWAY_LABEL_VALUE,
    ISTIO_INGRESSGATEWAY_NAMESPACE,
    RESEMBLE_GATEWAY_NAME,
    RESEMBLE_GATEWAY_ROUTING_FILTER_NAME,
    RESEMBLE_GATEWAY_VIRTUAL_SERVICE_NAME,
    RESEMBLE_MESH_ROUTING_FILTER_NAME,
    RESEMBLE_MESH_VIRTUAL_SERVICE_NAME,
    RESEMBLE_ROUTABLE_HOSTNAME,
    USER_CONTAINER_PORT,
)
from resemble.controller.virtual_service import (
    VirtualService,
    VirtualServiceSpec,
)
from resemble.v1alpha1 import placement_planner_pb2
from resemble.v1alpha1.istio.virtual_service_spec_pb2 import (
    Destination,
    HTTPMatchRequest,
    HTTPRoute,
    HTTPRouteDestination,
    PortSelector,
    StringMatch,
)
from resemble.v1alpha1.placement_planner_pb2 import ConsensusAddress
from respect.logging import get_logger
from typing import Coroutine, Optional

logger = get_logger(__name__)


class KubernetesNetworkManager:
    """The KubernetesNetworkManager is the part of the controller that is
    responsible for managing the network configuration of the cluster. Most
    notably, it will create the `VirtualService` and `EnvoyFilter` objects
    needed to route traffic from resemble clients to the appropriate consensuses
    for serving.
    """

    def __init__(
        self,
        k8s_client: AbstractEnhancedKubernetesClient,
        placement_planner: PlacementPlanner,
        own_pod_metadata: kubernetes_asyncio.client.V1ObjectMeta,
    ):
        self._k8s_client = k8s_client
        self._own_pod_metadata = own_pod_metadata
        self._namespace = own_pod_metadata.namespace
        self._consensus_address_by_name: dict[ConsensusName,
                                              ConsensusAddress] = {}
        self._consensus_name_by_service_name: dict[ServiceName,
                                                   ConsensusName] = {}

        self._placement_planner = placement_planner
        self.plan_version = -1
        self._plan_processed = asyncio.Event()
        self._stop_event = asyncio.Event()

    async def wait_for_plan_version(self, version: int):
        """Returns once a placement plan with the given version number (or
        higher) has been processed, which may be immediately. If the task that
        should produce the next plan fails, this will raise the error."""
        while True:  # Keep going until we get the right plan version.
            if self.plan_version >= version:
                return

            #############################################################
            # NOTE: between here and calling
            # `self._plan_processed.wait()` below we can not do any
            # `await`s or make other blocking calls which may yield
            # control because then it's possible that
            # `self.plan_version` will have been changed and/or
            # `self._plan_processed` will get set and cleared and
            # we'll miss the event and wait on
            # `self._plan_processed.wait()` indefinitely.
            #############################################################

            # We're not at the right version yet. We'll have to wait for a next
            # version to be processed.
            if not self.is_registered_for_callbacks():
                raise ValueError(
                    'The KubernetesNetworkManager is not running.'
                )
            # Make a local copy of `self._plan_processing_task`, since `stop()` can set the
            # object-level one to `None`, and we wouldn't be able to check
            # whether it is in the `done` set below, nor call `.result()` on it.
            plan_processing_task = self._plan_processing_task
            next_plan_processed_task = asyncio.create_task(
                self._plan_processed.wait()
            )
            # Wait for either...
            # (A) The next plan to be processed, or...
            # (B) The task that should produce the next plan to fail.
            done, _ = await asyncio.wait(
                [next_plan_processed_task, plan_processing_task],
                return_when=asyncio.FIRST_COMPLETED,
            )
            if plan_processing_task in done:
                # The task that should produce the first plan failed. We should
                # reraise the error. Calling `result()` will do that.
                plan_processing_task.result()
                # If we get here, the background task did complete, but didn't
                # raise an error. That's unexpected; it should run forever.
                raise ValueError(
                    'The KubernetesNetworkManager is in an illegal state: '
                    'Its background task completed without raising an error.'
                )

    async def run(self) -> None:
        """Syntactic sugar for `start` and `wait`."""
        await self.start()
        await self.wait()

    async def wait(self) -> None:
        """Wait until we have stopped."""
        await self._stop_event.wait()

    async def _process_plan_with_locations(
        self, plan_with_locations: placement_planner_pb2.PlanWithLocations
    ) -> None:
        """Process a new plan-with-locations as received either via callback or
        over RPC."""

        self.plan_version = plan_with_locations.plan.version
        logger.debug(
            'Received new plan with '
            f'{len(plan_with_locations.locations)} consensuses'
        )

        # Assemble a list of consensuses, their namespace, addresses, and the
        # services they host.
        # ISSUE(https://github.com/reboot-dev/respect/issues/1452): Replace
        # proto message Consensus with python object. This would help simplify
        # this data structure.
        consensuses: list[tuple[KubernetesNamespace, ConsensusName,
                                ConsensusAddress, list[ServiceName]]] = []
        for location in plan_with_locations.locations:
            consensus_name = location.consensus_name
            consensus_address = location.addresses[0]
            service_names: list[ServiceName] = []
            application_namespace: KubernetesNamespace = location.kubernetes_namespace
            if application_namespace == '':
                raise ValueError(
                    f'Missing kubernetes namespace for consensus: {consensus_name}'
                )

            for service_plan in plan_with_locations.plan.service_plans:
                for partition_assignment in service_plan.partition_assignments:
                    if partition_assignment.consensus_name == consensus_name:
                        service_names.append(service_plan.service_name)
                        break  # Add each service only once.

            consensuses.append(
                (
                    application_namespace,
                    consensus_name,
                    consensus_address,
                    service_names,
                )
            )

        # Update our internal view of the world to match the new consensuses.
        await self._set_consensuses(consensuses)

        # Indicate to anyone currently listening that a plan has been processed.
        # Then immediately clear it again, so future listeners block until the
        # next plan is processed.
        self._plan_processed.set()
        self._plan_processed.clear()
        logger.debug('Waiting for next plan...')

    def is_registered_for_callbacks(self) -> bool:
        return self._process_plan_with_locations in self._placement_planner.plan_change_callbacks

    async def start(self) -> None:
        """Subscribe to changes in the placement planner and start
        processing callbacks."""
        logger.debug('Starting KubernetesNetworkManager')

        # Subscribe to new plans.
        self._placement_planner.plan_change_callbacks.add(
            self._process_plan_with_locations
        )

        # Eagerly process latest plan.
        await self._process_plan_with_locations(
            self._placement_planner.current_plan_with_locations
        )

    def stop(self) -> None:
        """Unsubscribe from placement planner updates and stop processing
        callbacks."""
        logger.debug('Stopping KubernetesNetworkManager')

        # Unsubscribe from new plans.
        self._placement_planner.plan_change_callbacks.remove(
            self._process_plan_with_locations
        )

        # Notify all waiters that we are done.
        self._stop_event.set()

    def _make_virtual_service(self, name: str, gateway: str,
                              hosts: list[str]) -> Optional[VirtualService]:
        """Produces the `VirtualService` object appropriate for the Resemble
        gateway."""
        # Every consensus gets...
        # 1. An Istio `HTTPMatchRequest` that describes what HTTP requests
        #    should be routed to it. In our case, this looks for the header
        #    `x-resemble-consensus-id` with the value of the consensus' name.
        # 2. An Istio `HTTPRouteDestination` that describes where the request
        #    should go if it matches. In our case, that's the consensus'
        #    address.
        # For example, we may have an `HTTPMatchRequest` that looks like:
        #   HTTPMatchRequest(
        #       headers={
        #           'x-resemble-consensus-id': StringMatch(exact='consensus-1')
        #       }
        #   )
        # And its `HTTPRouteDestination` which looks like:
        #   HTTPRouteDestination(
        #       destination=Destination(
        #           host='consensus-1',
        #           port=PortSelector(number=5000)
        #       )
        #   )
        # There is exactly one such pair for each consensus.
        match_route_pairs_by_name: dict[ConsensusName,
                                        tuple[HTTPMatchRequest,
                                              HTTPRouteDestination]] = {}
        for consensus_name, consensus_address in self._consensus_address_by_name.items(
        ):
            match = HTTPMatchRequest(
                headers={
                    CONSENSUS_ID_HEADER: StringMatch(exact=consensus_name)
                }
            )
            route = HTTPRouteDestination(
                destination=Destination(
                    host=consensus_address.host,
                    port=PortSelector(number=consensus_address.port)
                )
            )
            match_route_pairs_by_name[consensus_name] = (match, route)

        if len(match_route_pairs_by_name) == 0:
            # If there are no consensuses, we don't need a VirtualService.
            # We also can't create an empty one; a VirtualService is required to
            # have at least one entry in its "http" list.
            return None

        return VirtualService(
            metadata=kubernetes_asyncio.client.V1ObjectMeta(
                namespace=self._namespace, name=name
            ),
            spec=VirtualServiceSpec(
                gateways=[gateway],
                hosts=hosts,
                http=[
                    HTTPRoute(
                        name=f'route-to-{consensus_name}',
                        match=[match],
                        route=[route],
                    )
                    for consensus_name, (match, route
                                        ) in match_route_pairs_by_name.items()
                ]
            )
        )

    def _make_virtual_service_for_mesh_traffic(
        self,
        name: str,
    ) -> Optional[VirtualService]:
        """Produces the `VirtualService` object appropriate for the current set
        of consensuses.
        """
        # The VirtualService we're constructing is intended to be applied to the
        # `mesh` gateway, which means: all sidecars in the Istio mesh. It is
        # then configured to (only) act on traffic routed to resemble's "routable
        # hostname". For a discussion on why that is, see the comments in
        # `_make_virtual_service_for_gateway_traffic()`.
        return self._make_virtual_service(
            name=name,
            gateway=ISTIO_ALL_SIDECARS_GATEWAY_NAME,
            hosts=[
                # The hostname without namespace is used by traffic that
                # has a `Service` with this name in their own namespace.
                RESEMBLE_ROUTABLE_HOSTNAME,
                # The hostname with namespace is used by traffic that does
                # not have a `Service` with this name in their own
                # namespace.
                f'{RESEMBLE_ROUTABLE_HOSTNAME}.{self._namespace}',
                # It's also allowed to specify the hostname with the full
                # Kubernetes domain name.
                f'{RESEMBLE_ROUTABLE_HOSTNAME}.{self._namespace}.svc.cluster.local',
            ]
        )

    def _make_virtual_service_for_gateway_traffic(
        self,
        name: str,
    ) -> Optional[VirtualService]:
        """Produces the `VirtualService` object appropriate for the gateways.
        """
        # The VirtualService we're constructing is intended to be applied to the
        # `resemble-gateway` gateway, which runs on the Istio ingress gateways.
        # There (and ONLY there) we want to accept traffic routed to any
        # hostname, most notably the hostnames the ingress gateways may use.
        #
        # This is a separate VirtualService from the one that handles mesh
        # traffic, because it's important that ONLY the gateways handle traffic
        # addressed to the gateways. It would be incorrect for sidecars in the
        # Istio mesh to handle gateway-bound traffic: gateway traffic likely
        # comes from pods that are part of the Istio mesh but are NOT part of a
        # Resemble application. Such pods do execute all `mesh` VirtualServices
        # (whose scope is all namespaces in the Istio mesh) but DON'T run the
        # Resemble routing filters (whose scope is all namespaces in a Resemble
        # application). It is a requirement for Resemble traffic that the
        # Resemble routing filter be applied before a VirtualService is
        # executed. On pods that don't run the routing filter, we must therefore
        # avoid having a `mesh` VirtualService that acts on the traffic. We do
        # this by scoping down the `mesh` VirtualService to only act on traffic
        # that is explicitly addressed to the Resemble routable hostname (which
        # is only ever used by Resemble applications), and not on traffic routed
        # to the Resemble gateways (which is used by non-Resemble applications).
        #
        # Instead, the VirtualService for mesh traffic will ignore traffic to
        # the gateways, allowing the gateways to do routing on behalf of these
        # non-Resemble pods. The following VirtualService is the one that will
        # do that routing on the gateways.
        #
        # Once traffic is at the gateway, we accept all traffic directed to all
        # hosts. That includes hostnames we've never heard of, since the
        # operator may have configured the ingress gateway with a hostname we
        # have no knowledge of.
        return self._make_virtual_service(
            name=name,
            gateway=RESEMBLE_GATEWAY_NAME,
            hosts=["*"],
        )

    async def _write_or_delete_virtual_service(
        self, name: str, virtual_service: Optional[VirtualService]
    ):
        if virtual_service is None:
            # Delete the VirtualService if it exists.
            logger.debug(f'No VirtualService needed; deleting existing {name}')
            await self._k8s_client.custom_objects.delete_by_name(
                namespace=self._namespace,
                name=name,
                object_type=VirtualService,
            )
            return
        logger.debug(f'Writing VirtualService: {virtual_service.to_dict()}')
        await self._k8s_client.custom_objects.create_or_update(virtual_service)

    async def _write_virtual_services(self):
        """Writes the latest `VirtualService`s to Kubernetes."""
        # There are two VirtualServices: one for (Istio) mesh traffic (applied
        # to Istio's `mesh` gateway which deploys it on every sidecar in every
        # namespace that's part of Istio's mesh), and one for (Resemble) gateway
        # traffic (applied to the `resemble-gateway` gateway, which deploys it
        # ONLY on ingress gateway pods).
        #
        # The `mesh` VirtualService routes traffic from Resemble actors to other
        # Resemble actors point-to-point - thanks to the routing by the sidecars
        # we don't need to route through the gateways. This saves a hop, which
        # is important for performance: otherwise the gateways would have to
        # scale up with the intra-Resemble traffic, which will be a different
        # order of magnitude than the external traffic they're required to
        # handle.
        #
        # The `resemble-gateway` VirtualService routes traffic that's arrived at
        # a Gateway. It makes the same decisions as the `mesh` VirtualService,
        # but does so at a different place.
        #
        # These VirtualServices are separate, because it would be incorrect for
        # sidecars in the Istio mesh to act on gateway-bound traffic: gateway
        # traffic likely comes from pods that are part of the Istio mesh but are
        # NOT part of a Resemble application. Such pods do execute all `mesh`
        # VirtualServices (whose scope is all namespaces in the Istio mesh) but
        # DON'T run the Resemble routing filters (since the `EnvoyFilter`s that
        # configure those are scoped to only those namespaces that are also in a
        # Resemble application). It is a requirement for Resemble traffic that
        # the Resemble routing filter be applied before their VirtualService is
        # executed. On pods that don't run the routing filter, we must therefore
        # avoid having a VirtualService that acts on the traffic. We do this by
        # scoping down the `mesh` VirtualService to only act on traffic that is
        # explicitly addressed to the Resemble "routable hostname" (which is a
        # Resemble-internal name only ever used by Resemble applications), and
        # not on traffic routed to the Resemble gateways (which is used by
        # non-Resemble applications). The traffic bound for the Resemble
        # gateways will be run through the routing filter and
        # `resemble-gateway`'s virtual service once it reaches the gateway.
        name = RESEMBLE_MESH_VIRTUAL_SERVICE_NAME
        await self._write_or_delete_virtual_service(
            name, self._make_virtual_service_for_mesh_traffic(name)
        )
        name = RESEMBLE_GATEWAY_VIRTUAL_SERVICE_NAME
        await self._write_or_delete_virtual_service(
            name, self._make_virtual_service_for_gateway_traffic(name)
        )

    async def _write_routing_filters_for_internal_traffic(
        self, namespaces: set[KubernetesNamespace]
    ):
        """Writes the latest routing filter `EnvoyFilter` for internal (that is:
        Consensus-to-Consensus) traffic to Kubernetes.

        The argument `namespaces` specifies the kubernetes namespaces that
        should contain a routing filter. Our routing filter in these namespaces
        will be created or updated, while routing filters previously created by
        us in other namespaces will be deleted.
        """

        # A set of envoy filters that are no longer needed; we need to remove
        # these.
        obsolete_routing_filters: list[EnvoyFilter] = []

        # Find ALL the EnvoyFilters!
        existing_routing_filters = await self._k8s_client.custom_objects.list_all(
            object_type=EnvoyFilter,
        )
        logger.debug(
            'Found %i routing filters...', len(existing_routing_filters)
        )

        # Loop over them, check if they are a) ours, b) desired.
        for existing_routing_filter in existing_routing_filters:
            name = existing_routing_filter.metadata.name
            namespace = existing_routing_filter.metadata.namespace

            if name != RESEMBLE_MESH_ROUTING_FILTER_NAME:
                # Not one of ours, skip.
                logger.debug(
                    "EnvoyFilter that is not a routing filter '%s' "
                    "encountered. Ignoring.", name
                )
                continue

            if namespace in namespaces:
                # We want to update this one, not remove it.
                logger.debug(
                    'Envoy filter in namespace %s should remain. Ignoring',
                    namespace
                )
                continue

            # Mark namespace for cleanup.
            obsolete_routing_filters.append(existing_routing_filter)

        # Remove our obsolete envoy filters.
        if len(obsolete_routing_filters) > 0:
            logger.info(
                'Removing envoy filter %s from the following namespaces: %s',
                RESEMBLE_MESH_ROUTING_FILTER_NAME,
                [
                    obsolete.metadata.namespace
                    for obsolete in obsolete_routing_filters
                ],
            )
            await asyncio.gather(
                *[
                    self._k8s_client.custom_objects.delete(obsolete)
                    for obsolete in obsolete_routing_filters
                ]
            )
        else:
            logger.info('No obsolete routing filters found')

        logger.info(
            'Writing routing filter to the following namespaces: %s',
            namespaces,
        )
        creations: list[Coroutine] = []
        for namespace in namespaces:
            # Get the `EnvoyFilter` representing our routing filter. That
            # object's `.metadata.name` is always the same, so we can safely use
            # `create_or_update` to update any previous version in-place.
            routing_filter: EnvoyFilter = generate_istio_routing_filter(
                namespace=namespace,
                name=RESEMBLE_MESH_ROUTING_FILTER_NAME,
                consensuses_by_service=self._consensus_name_by_service_name,
                context=FilterContext.MESH,
            )
            logger.debug(f'Routing filter body: {routing_filter.to_dict()}')
            creations.append(
                self._k8s_client.custom_objects.
                create_or_update(routing_filter)
            )

        await asyncio.gather(*creations)

    async def _write_routing_filter_for_gateway_traffic(self):
        # Get the `EnvoyFilter` representing our routing filter. That object's
        # `.metadata.name` is always the same, so we can safely use
        # `create_or_update` to update any previous version in-place.
        routing_filter: EnvoyFilter = generate_istio_routing_filter(
            namespace=ISTIO_INGRESSGATEWAY_NAMESPACE,
            name=RESEMBLE_GATEWAY_ROUTING_FILTER_NAME,
            consensuses_by_service=self._consensus_name_by_service_name,
            context=FilterContext.GATEWAY,
        )
        logger.debug(
            f'Writing gateway routing filter: {routing_filter.to_dict()}'
        )
        await self._k8s_client.custom_objects.create_or_update(routing_filter)

    async def _write_routable_service(self):
        """Writes the Kubernetes `Service` that gives us a single routable
        hostname for all services (and therefore actors) in the system.
        """
        await self._k8s_client.services.create_or_update(
            # There is one routable service for the entire Resemble system, so
            # we'll put it in the resemble system's own namespace.
            namespace=self._namespace,
            # The name of the routable service is a well-known string that all
            # clients use to contact any Resemble service.
            name=RESEMBLE_ROUTABLE_HOSTNAME,
            # The port on which the routable service is reached is universally
            # known also.
            port=USER_CONTAINER_PORT,
            # To let this port serve gRPC traffic when there's an intermediate
            # Envoy proxy in gateway mode, this port MUST be called "grpc".
            port_name="grpc",
            # We only need the routable service's hostname to exist and resolve,
            # it doesn't (shouldn't) point at any pods.
            deployment_label=None,
            # Unlike other objects created by the controller, this `Service`
            # isn't tied to a user action; it's an always-present part of the
            # system itself. Therefore, the controller itself is the owner of
            # the object.
            owner=OwnershipInformation.from_metadata(
                kind='Pod',
                api_version='v1',
                metadata=self._own_pod_metadata,
            )
        )

    async def _write_gateway(self):
        """Writes the Kubernetes `Gateway` that allows external traffic to
        reach the Resemble system.
        """
        # The Gateway object is an Istio configuration that instructs the Istio
        # gateway to accept traffic on a particular port. It also gives traffic
        # received on that port a name, which is used by VirtualServices to
        # name the traffic they'd like to be routing.
        await self._k8s_client.custom_objects.create_or_update(
            Gateway(
                metadata=kubernetes_asyncio.client.V1ObjectMeta(
                    namespace=self._namespace,
                    name=RESEMBLE_GATEWAY_NAME,
                ),
                spec=GatewaySpec(
                    selector={
                        ISTIO_INGRESSGATEWAY_LABEL_NAME:
                            ISTIO_INGRESSGATEWAY_LABEL_VALUE
                    },
                    servers=[
                        gateway_spec_pb2.Server(
                            # Accept traffic for all hosts. We assume that if
                            # traffic can reach the gateway, we want to handle
                            # it.
                            hosts=['*'],
                            # Accept traffic on the following port.
                            #
                            # ISSUE(1529): this configures the gateway to accept
                            # (only) unencrypted traffic. Allow the user to
                            # configure their gateway to use TLS.
                            port=gateway_spec_pb2.Port(
                                number=ISTIO_INGRESSGATEWAY_INTERNAL_PORT,
                                name='grpc',
                                protocol='GRPC',
                            )
                        )
                    ]
                )
            )
        )

    async def _set_consensuses(
        self, consensuses: list[tuple[KubernetesNamespace, ConsensusName,
                                      ConsensusAddress, list[ServiceName]]]
    ):
        """Sets the list of consensuses that the network manager knows about.
        Each entry in the list represents one consensus, and is a tuple of
        (consensus_name, consensus_address, service_names). The service_names
        are the names of the services that the consensus is responsible for.
        """
        self._consensus_address_by_name = {
            name: address for _, name, address, __ in consensuses
        }
        self._consensus_name_by_service_name = {
            service_name: consensus_name
            for _, consensus_name, __, service_name_list in consensuses
            for service_name in service_name_list
        }

        # The routable service gives clients a hostname to connect to when
        # they want to talk to Resemble.
        await self._write_routable_service()

        # The Gateway allows external traffic to reach the Resemble system.
        await self._write_gateway()

        # The routing filter will select a consensus and set a consensus name
        # header based on the targeted service name and actor ID.
        namespaces = {namespace for namespace, _, __, ___ in consensuses}
        await self._write_routing_filters_for_internal_traffic(namespaces)
        await self._write_routing_filter_for_gateway_traffic()

        # The VirtualServices direct connections to the appropriate consensus
        # based on their consensus name header.
        await self._write_virtual_services()
