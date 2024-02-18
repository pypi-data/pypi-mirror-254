from contextvars import ContextVar
from enum import Enum

# Python asyncio context variable that stores whether or not the
# current context is servicing an RPC, i.e., is "inside" of an
# actor. We use INITIALIZING to distinguish when a Context is
# permitted to be constructed.
Servicing = Enum('Servicing', [
    'NO',
    'INITIALIZING',
    'YES',
])

_servicing: ContextVar[Servicing] = ContextVar(
    'RPC servicing status of current asyncio context', default=Servicing.NO
)
