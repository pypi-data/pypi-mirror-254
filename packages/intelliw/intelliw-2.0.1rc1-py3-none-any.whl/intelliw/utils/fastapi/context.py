from copy import deepcopy

from intelliw.utils.fastapi import _request_scope_context_storage
from contextvars import copy_context


class _Context:

    @staticmethod
    def get():
        try:
            return _request_scope_context_storage.get()
        except LookupError as e:
            raise RuntimeError(
                "You didn't use ContextMiddleware or "
                "you're trying to access `context` object "
                "outside of the request-response cycle."
            ) from e

    @staticmethod
    def copy_set(data):
        return _request_scope_context_storage.set(
            deepcopy(data)
        )

    @staticmethod
    def set(data):
        return _request_scope_context_storage.set(
            data
        )

    @staticmethod
    def exists() -> bool:
        return _request_scope_context_storage in copy_context()


context = _Context()
