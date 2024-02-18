from contextvars import ContextVar

_request_scope_context_storage: ContextVar[str] = ContextVar(
    "ctx", default=None
)
