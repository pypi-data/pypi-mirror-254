import asyncio
import grpc
import logging
import traceback
import websockets
from google.protobuf.json_format import MessageToJson
from google.rpc import code_pb2, status_pb2
from grpc_status import rpc_status
from resemble.aio.errors import Aborted, Error, UnknownService
from resemble.aio.headers import Headers
from resemble.aio.internals.middleware import Middleware
from resemble.aio.types import ServiceName
from resemble.settings import LOCALHOST_LISTEN_ADDRESS
from resemble.v1alpha1 import react_pb2, react_pb2_grpc
from respect.logging import get_logger
from typing import AsyncIterable, Optional

logger = get_logger(__name__)

# We set the log level to `ERROR` here because websockets is chatty!
logger.setLevel(logging.ERROR)


class ReactServicer(react_pb2_grpc.ReactServicer):
    """System service for serving requests from our code generated react
    readers.

    TODO(benh): make this more generic than just for react so that
    users and other system services (e.g., a read cache) can use this
    to get reactive/streaming reads without the user having to
    implement it themselves.
    """

    def __init__(
        self, middleware_by_service_name: dict[ServiceName, Middleware]
    ):
        self._middleware_by_service_name = middleware_by_service_name

        self._stop_websockets_serve = asyncio.Event()

    async def start(self) -> int:
        """Starts the websocket server and returns the port that it is
        listening on."""
        port: asyncio.Future[int] = asyncio.Future()

        async def websockets_serve():
            async with websockets.serve(
                self.serve, LOCALHOST_LISTEN_ADDRESS, logger=logger
            ) as server:
                # server.sockets is of type Iterable[socket] but is not
                # guaranteed to be an indexable list.
                socket = next(iter(server.sockets))
                port.set_result(socket.getsockname()[1])
                await self._stop_websockets_serve.wait()

        self._websockets_serve_task = asyncio.create_task(websockets_serve())

        await port

        return port.result()

    async def stop(self):
        self._stop_websockets_serve.set()
        try:
            await self._websockets_serve_task
        except:
            # We're trying to stop so no need to propagate any
            # exceptions.
            pass

    async def serve(self, websocket):
        # Expected path: /__/resemble/websocket/service_name/actor_id
        #
        # After split: ['', '__', 'resemble' 'websocket', 'service_name', 'actor_id']
        service_name, actor_id = websocket.path.split('/')[4:6]

        middleware: Optional[Middleware] = (
            self._middleware_by_service_name.get(service_name)
        )

        if middleware is None:
            logger.error(
                "Attempted to perform a 'React' mutate to an unknown "
                f"service '{service_name}'; "
                "did you bring up a servicer for it in your `Application`?"
            )
            raise Error(UnknownService())

        try:
            async for request_bytes in websocket:
                try:
                    request = react_pb2.MutateRequest()
                    request.ParseFromString(request_bytes)

                    response = await middleware.react_mutate(
                        actor_id,
                        request.method,
                        request.request,
                        request.idempotency_key,
                        request.bearer_token
                        if request.HasField('bearer_token') else None,
                    )

                    await websocket.send(
                        react_pb2.MutateResponse(
                            response=response.SerializeToString()
                        ).SerializeToString()
                    )
                except asyncio.CancelledError:
                    # It's pretty normal for a query to be cancelled; it's not useful to
                    # print a stack trace.
                    raise
                except grpc.aio.BaseError:
                    # If somewhere deeper in the call graph had a gRPC error
                    # just let that propagate!
                    raise
                except Aborted as aborted:
                    status = aborted.to_status(
                        # NOTE: we don't pass `error_type` which means
                        # we'll get a different error message than
                        # when an error is returned within Resemble.
                    )
                    await websocket.send(
                        react_pb2.MutateResponse(status=MessageToJson(status)
                                                ).SerializeToString()
                    )
                except BaseException as exception:
                    # Print the exception stack trace for easier
                    # debugging. Note that we don't include the stack
                    # trace in an error message for the same reason
                    # that gRPC doesn't do so by default, see
                    # https://github.com/grpc/grpc/issues/14897, but
                    # since this should only get logged on the server
                    # side it is safe.
                    traceback.print_exc()

                    # TODO: send a status which does not include any
                    # details, just a message which we glean from the
                    # raised exception.
                    status = status_pb2.Status(
                        code=code_pb2.Code.UNKNOWN,
                        message=f'{type(exception).__name__}: {exception}',
                    )
                    await websocket.send(
                        react_pb2.MutateResponse(status=MessageToJson(status)
                                                ).SerializeToString()
                    )
        except websockets.exceptions.ConnectionClosedOK:
            # No real error here, browser users will come and go!
            pass
        except websockets.exceptions.ConnectionClosedError:
            # No real error here, browser users may get disconnected!
            pass
        except:
            # For now we print these out so we can debug if necessary.
            traceback.print_exc()

    def add_to_server(self, server: grpc.aio.Server) -> None:
        react_pb2_grpc.add_ReactServicer_to_server(self, server)

    async def Query(
        self,
        request: react_pb2.QueryRequest,
        grpc_context: grpc.aio.ServicerContext,
    ) -> AsyncIterable[react_pb2.QueryResponse]:
        """Implements the React.Query RPC that calls into the
        'Middleware.react' method for handling the request."""
        try:
            headers = Headers.from_grpc_context(grpc_context)

            middleware: Optional[Middleware] = (
                self._middleware_by_service_name.get(headers.service_name)
            )

            if middleware is None:
                logger.error(
                    "Attempted to perform a 'React' query to an unknown "
                    f"service '{headers.service_name}'; "
                    "did you bring up a servicer for it in your `Application`?"
                )
                raise Error(UnknownService())

            async for (response, idempotency_keys) in middleware.react_query(
                grpc_context,
                headers.actor_id,
                request.method,
                request.request,
                headers.bearer_token,
            ):
                yield react_pb2.QueryResponse(
                    response=(
                        response.SerializeToString()
                        if response is not None else None
                    ),
                    idempotency_keys=[
                        str(idempotency_key)
                        for idempotency_key in idempotency_keys
                    ],
                )
        except asyncio.CancelledError:
            # It's pretty normal for a query to be cancelled; it's not useful to
            # print a stack trace.
            raise
        except grpc.aio.BaseError:
            # If somewhere deeper in the call graph had a gRPC error
            # just let that propagate!
            raise
        except Aborted as aborted:
            await grpc_context.abort_with_status(
                rpc_status.to_status(
                    aborted.to_status(
                        # NOTE: we don't pass `error_type` which means
                        # we'll get a different error message than
                        # when an error is returned within Resemble.
                    )
                )
            )
        except BaseException as exception:
            # Don't print a stack trace for any common errors or user
            # errors that were raised that we turned into an
            # `Aborted`. We should have logged an error to make it
            # easier for a user to debug.
            #
            # As of the writing of this comment we know that if the
            # context status code is `ABORTED` then it must have been
            # from our `Aborted` because there aren't any other ways
            # for Resemble apps to abort an RPC because we don't give
            # them access to a `ServicerContext`. But even if we do,
            # if a user calls abort then that's similar to raising one
            # of their user errors and we probably don't need to print
            # a stack trace.
            if (
                grpc_context.code() != code_pb2.Code.ABORTED and
                not isinstance(exception, GeneratorExit)
            ):
                traceback.print_exc()

            raise exception

    async def WebSocketsConnection(
        self,
        request: react_pb2.WebSocketsConnectionRequest,
        grpc_context: grpc.aio.ServicerContext,
    ) -> react_pb2.WebSocketsConnectionResponse:
        await asyncio.Event().wait()
        # TODO(benh): use `assert_never` in Python > 3.11.
        assert False, 'Unreachable'
