from __future__ import annotations

import grpc
import uuid
from dataclasses import dataclass
from resemble.aio.types import ActorId, GrpcMetadata, ServiceName
from typing import Any, Callable, Optional

# This code ties in with the concept of a Context. There are a lot of open
# questions about what information is carried on a context and how it is
# represented and transmitted. We believe that the Context need to contain
# information about the full call DAG, but it is currently unclear how this
# information should be encoded. Similarly, it is unclear how this information
# should be transmitted. We believe that gRPC metadata is the correct way of
# transmitting this data but the encoding of the DAG into gRPC metadata is not
# well understood.
#
# From the full call DAG information, it should be possible to obtain various
# information that is needed by the Context, such as the current safety level,
# the actor that is currently being served, etc. Until we have a better idea for
# how we are a) representing these and b) encoding them into metadata headers,
# we are "cherry picking" the necessary DAG information and sticking it on
# individual headers.
#
# This small library is intended as an abstraction layer to provide the ability
# to encode and decode DAG information as grpc headers without having to care
# too much about the current implementation.

# If ever these header constants change, also update their invariant
# counterparts in tests/local_envoy_config.yaml.j2.
# The header that tells us what service we're targeting.
SERVICE_NAME_HEADER = 'x-resemble-service-name'
# The header that carries actor id information.
ACTOR_ID_HEADER = 'x-resemble-actor-id'
# The header that carries information about which consensus this request should
# be handled by.
CONSENSUS_ID_HEADER = 'x-resemble-consensus-id'

# Transaction related headers.
TRANSACTION_ID_HEADER = 'x-resemble-transaction-id'
TRANSACTION_COORDINATOR_SERVICE_HEADER = 'x-resemble-transaction-coordinator-service'
TRANSACTION_COORDINATOR_ACTOR_ID_HEADER = 'x-resemble-transaction-coordinator-actor-id'
TRANSACTION_PARTICIPANTS_HEADER = 'x-resemble-transaction-participants'

# The header that carries the idempotency key for a mutation.
#
# TODO(benh): investigate using the proposed 'Idempotency-Key' header
# instead:
# https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header
IDEMPOTENCY_KEY_HEADER = 'x-resemble-idempotency-key'

AUTHORIZATION_HEADER = 'authorization'


@dataclass(kw_only=True)
class Headers:
    """Dataclass for working with resemble metadata headers.
    """
    service_name: ServiceName
    actor_id: ActorId
    transaction_id: Optional[uuid.UUID] = None
    transaction_coordinator_service: Optional[str] = None
    transaction_coordinator_actor_id: Optional[str] = None

    idempotency_key: Optional[uuid.UUID] = None

    bearer_token: Optional[str] = None

    @classmethod
    def from_grpc_context(
        cls,
        grpc_context: grpc.aio.ServicerContext,
    ) -> Headers:
        """Convert and parse gRPC metadata to `Headers`."""
        # Extract the raw gRPC metadata from gRPC context to dictionary.
        raw_headers = dict(grpc_context.invocation_metadata())

        def extract_maybe(
            name: str,
            *,
            required=False,
            convert: Callable[[str], Any] = lambda value: value
        ) -> Optional[Any]:
            try:
                return convert(raw_headers[name])
            except KeyError as e:
                if required:
                    raise ValueError(f"gRPC metadata missing '{name}'") from e
                else:
                    return None

        def extract(
            name: str,
            *,
            convert: Callable[[str], Any] = lambda value: value
        ) -> Any:
            return extract_maybe(name, required=True, convert=convert)

        service_name = extract(SERVICE_NAME_HEADER)
        actor_id = extract(ACTOR_ID_HEADER)

        transaction_id: Optional[uuid.UUID] = extract_maybe(
            TRANSACTION_ID_HEADER, convert=lambda value: uuid.UUID(value)
        )

        transaction_coordinator_service: Optional[str] = extract_maybe(
            TRANSACTION_COORDINATOR_SERVICE_HEADER,
            required=transaction_id is not None
        )

        transaction_coordinator_actor_id: Optional[str] = extract_maybe(
            TRANSACTION_COORDINATOR_ACTOR_ID_HEADER,
            required=transaction_id is not None
        )

        idempotency_key: Optional[uuid.UUID] = extract_maybe(
            IDEMPOTENCY_KEY_HEADER,
            convert=lambda value: uuid.UUID(value),
        )

        bearer_token: Optional[str] = extract_maybe(
            AUTHORIZATION_HEADER,
            convert=lambda value: value.removeprefix('Bearer '),
        )

        return cls(
            service_name=service_name,
            actor_id=actor_id,
            transaction_id=transaction_id,
            transaction_coordinator_service=transaction_coordinator_service,
            transaction_coordinator_actor_id=transaction_coordinator_actor_id,
            idempotency_key=idempotency_key,
            bearer_token=bearer_token,
        )

    def to_grpc_metadata(self) -> GrpcMetadata:
        """Encode these headers as gRPC metadata."""

        def maybe_add_authorization_header() -> GrpcMetadata | tuple[()]:
            if self.bearer_token is not None:
                return (
                    (AUTHORIZATION_HEADER, f'Bearer {self.bearer_token}'),
                )
            return ()

        def maybe_add_transaction_headers() -> GrpcMetadata | tuple[()]:
            if self.transaction_id is not None:
                assert self.transaction_coordinator_service is not None
                assert self.transaction_coordinator_actor_id is not None
                return (
                    (TRANSACTION_ID_HEADER, str(self.transaction_id)),
                    (
                        TRANSACTION_COORDINATOR_SERVICE_HEADER,
                        self.transaction_coordinator_service
                    ),
                    (
                        TRANSACTION_COORDINATOR_ACTOR_ID_HEADER,
                        self.transaction_coordinator_actor_id
                    ),
                )
            return ()

        return (
            (
                (SERVICE_NAME_HEADER, self.service_name),
                (ACTOR_ID_HEADER, self.actor_id),
            ) + maybe_add_authorization_header() +
            maybe_add_transaction_headers()
        )
