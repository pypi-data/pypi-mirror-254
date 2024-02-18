import grpc
from grpc_interceptor.server import AsyncServerInterceptor
from resemble.aio.internals.channel_manager import _ChannelManager
from resemble.aio.workflows import Workflow
from typing import Any, Callable, Iterable, Mapping, Optional


class LegacyGrpcContext(grpc.aio.ServicerContext):
    """A subclass that Resemble will automatically substitute for
    grpc.aio.ServicerContext when forwarding traffic to RPCs in legacy gRPC
    servicers.

    Such servicers can then use this context to get a Workflow instance and send
    requests to other services in the Resemble system.
    """

    def __init__(
        self, original_context: grpc.aio.ServicerContext,
        channel_manager: _ChannelManager
    ):
        self._original_context = original_context
        self._channel_manager = channel_manager

    def workflow(self, name: str) -> Workflow:
        return Workflow(name=name, channel_manager=self._channel_manager)

    # Implement all the grpc.aio.ServicerContext interface methods by passing
    # through to self._original_context.
    async def read(self):
        return await self._original_context.read()

    async def write(self, message) -> None:
        await self._original_context.write(message)

    async def send_initial_metadata(self, initial_metadata) -> None:
        await self._original_context.send_initial_metadata(initial_metadata)

    async def abort(
        self,
        code: grpc.StatusCode,
        details: str = "",
        trailing_metadata=tuple(),
    ):
        return await self._original_context.abort(
            code, details, trailing_metadata
        )

    async def abort_with_status(self, status):
        return await self._original_context.abort_with_status(status)

    def set_trailing_metadata(self, trailing_metadata) -> None:
        self._original_context.set_trailing_metadata(trailing_metadata)

    def invocation_metadata(self):
        return self._original_context.invocation_metadata()

    def set_code(self, code: grpc.StatusCode) -> None:
        self._original_context.set_code(code)

    def set_details(self, details: str) -> None:
        self._original_context.set_details(details)

    def set_compression(self, compression: grpc.Compression) -> None:
        self._original_context.set_compression(compression)

    def disable_next_message_compression(self) -> None:
        self._original_context.disable_next_message_compression()

    def peer(self) -> str:
        return self._original_context.peer()

    def peer_identities(self) -> Optional[Iterable[bytes]]:
        return self._original_context.peer_identities()

    def peer_identity_key(self) -> Optional[str]:
        return self._original_context.peer_identity_key()

    def auth_context(self) -> Mapping[str, Iterable[bytes]]:
        return self._original_context.auth_context()

    def time_remaining(self) -> float:
        return self._original_context.time_remaining()

    def trailing_metadata(self):
        return self._original_context.trailing_metadata()

    def code(self):
        return self._original_context.code()

    def details(self):
        return self._original_context.details()

    def add_done_callback(self, callback) -> None:
        return self._original_context.add_done_callback(callback)

    def cancelled(self) -> bool:
        return self._original_context.cancelled()

    def done(self) -> bool:
        return self._original_context.done()


class ResembleContextInterceptor(AsyncServerInterceptor):

    def __init__(self, channel_manager: _ChannelManager):
        self._channel_manager = channel_manager

    async def intercept(
        self,
        method: Callable,
        request_or_iterator: Any,
        context: grpc.aio.ServicerContext,
        method_name: str,
    ) -> Any:
        resemble_grpc_context = LegacyGrpcContext(
            context, self._channel_manager
        )

        response_or_iterator = method(
            request_or_iterator, resemble_grpc_context
        )
        if not hasattr(response_or_iterator, "__aiter__"):
            # Unary, just await and return the response.
            return await response_or_iterator

        # Server streaming responses, delegate to an async generator helper.
        return self._intercept_streaming(response_or_iterator)

    async def _intercept_streaming(self, iterator):
        async for r in iterator:
            yield r
