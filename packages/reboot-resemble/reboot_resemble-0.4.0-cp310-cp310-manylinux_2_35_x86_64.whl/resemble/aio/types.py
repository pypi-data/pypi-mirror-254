from typing import Any

# Collection of types used throughout our code with more meaningful names than
# the underlying python types.

ActorId = str
ServiceName = str
ConsensusName = str
GrpcMetadata = tuple[tuple[str, str], ...]
RoutableAddress = str
KubernetesNamespace = str


def assert_type(t: Any, types: list[type[Any]]) -> None:
    """Check that 't' is an instance of one of the expected types.

    Raises TypeError if 't' is not one of the expected types.
    """
    if any([isinstance(t, expected_type) for expected_type in types]):
        return

    raise TypeError(
        f'{type(t).__name__} is not one of expected type(s): '
        f'{[expected_type.__name__ for expected_type in types]}'
    )
