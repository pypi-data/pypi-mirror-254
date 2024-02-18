from abc import ABC, abstractmethod
from google.protobuf.message import Message
from resemble.aio.contexts import ReaderContext
from typing import Optional


class Authorizer(ABC):
    """Abstract base class for general Servicer Authorizers.

    A Servicer's authorizer is used to determine whether a given call to a
    Servicer's methods should be allowed or not.
    """

    @abstractmethod
    async def authorize(
        self,
        *,
        method_name: str,
        context: ReaderContext,
        state: Optional[Message] = None,
        request: Optional[Message] = None,
    ) -> bool:
        """Determine whether a call to a the method @method_name should be
        allowed.

        :param method_name: The name of the method being called.
        :param context: A reader context to enable calling other services.
        :param state: The state where and when available.
        :param request: The request object to the servicer method being called.

        Returns:
            True if the call should be allowed, False otherwise.
        """
        # Sane default.
        return False

    @abstractmethod
    def can_authorize(self, method_name: str) -> bool:
        """Determine if the 'Authorizer' is fit for making an authorization
        decision for a given method name.
        """
        raise NotImplementedError
