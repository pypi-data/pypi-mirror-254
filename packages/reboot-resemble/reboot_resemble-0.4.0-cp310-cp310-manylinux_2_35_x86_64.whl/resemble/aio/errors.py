import grpc
from google.protobuf import any_pb2
from google.rpc import status_pb2
from resemble.aio.types import assert_type
from resemble.v1alpha1.errors_pb2 import (
    ActorAlreadyConstructed,
    ActorNotConstructed,
    PermissionDenied,
    Unauthenticated,
    UnknownService,
)
from typing import Optional, TypeVar, Union


class Aborted(Exception):
    """Base class of all RPC specific code generated errors used for
    aborting an RPC.

    NOTE: Given the issues[1] with multiple inheritance from `abc.ABC` and `Exception`
    we do not inherit from `abc.ABC` but raise `NotImplementedError` for
    "abstract" methods.

    [1] https://bugs.python.org/issue12029
    """

    def __init__(self):
        super().__init__()

    @property
    def detail(self):
        return NotImplementedError

    @property
    def code(self) -> grpc.StatusCode:
        return NotImplementedError

    @property
    def message(self):
        return NotImplementedError

    def to_status(
        self,
        error_type: Optional[type] = None,
    ) -> status_pb2.Status:
        detail = any_pb2.Any()
        detail.Pack(self.detail)

        message = self.message

        # We support propagating an expected error detail regardless
        # of the actual type of `self`, i.e., `self` here might be the
        # actual error type for a method, e.g., `Bar.SomeMethod.Error`
        # or it may be another error type, e.g.,
        # `Foo.AnotherMethod.Error`, because `Bar.SomeMethod` called
        # `Foo.AnotherMethod` but didn't catch the error. If the error
        # detail in this case is a declared error for this method we
        # will update the message to make it seem like it is coming
        # from `Bar.SomeMethod` since it declares the error.
        #
        # TODO(benh): revisit if we want to do this at all for now.
        if (
            error_type is not None and not isinstance(self, error_type) and
            error_type.is_declared_error(self.detail)
        ):
            message = f"{error_type.DEFAULT_MESSAGE}: {message}"

        return status_pb2.Status(
            # A `grpc.StatusCode` is a `tuple[int, str]` where the
            # `int` is the actual code that we need to pass on.
            code=self.code.value[0],
            message=message,
            details=[detail],
        )


AbortedT = TypeVar('AbortedT', bound=Aborted)


# TODO(benh): move this to `Aborted`.
def _from_status(
    cls: type[AbortedT],
    status: status_pb2.Status,
) -> Optional[AbortedT]:
    # TODO(rjh, benh): think about how to handle cases where there are
    # multiple errors (since there are multiple details).
    assert issubclass(cls, Aborted)

    for any in status.details:
        for detail_type in cls.DETAIL_TYPES:
            if any.Is(detail_type.DESCRIPTOR):
                detail = detail_type()
                any.Unpack(detail)

                # TODO(benh): figure out why we need to ignore this type.
                return cls(detail, message=status.message)  # type: ignore

    return None


class Error(Aborted):
    """Common errors."""

    # Type alias for the union of possible error details.
    Detail = Union[
        ActorAlreadyConstructed,
        ActorNotConstructed,
        PermissionDenied,
        Unauthenticated,
        UnknownService,
    ]

    DETAIL_TYPES: list[type[Detail]] = [
        ActorAlreadyConstructed,
        ActorNotConstructed,
        PermissionDenied,
        Unauthenticated,
        UnknownService,
    ]

    _detail: Detail
    _code: grpc.StatusCode
    _message: str

    def __init__(
        self,
        detail: Detail,
        *,
        code: grpc.StatusCode = grpc.StatusCode.ABORTED,
        message: Optional[str] = None,
    ):
        super().__init__()

        assert_type(detail, self.DETAIL_TYPES)

        self._detail = detail

        if isinstance(detail, PermissionDenied):
            self._code = grpc.StatusCode.PERMISSION_DENIED
        elif isinstance(detail, Unauthenticated):
            self._code = grpc.StatusCode.UNAUTHENTICATED
        else:
            self._code = code

        self._message = message or detail.DESCRIPTOR.name

    @property
    def detail(self) -> Detail:
        return self._detail

    @property
    def code(self) -> grpc.StatusCode:
        return self._code

    @property
    def message(self) -> str:
        return self._message

    @classmethod
    def from_status(cls, status: status_pb2.Status):
        return _from_status(cls, status)
