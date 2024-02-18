"""Helper decorators for ChessBoard."""

import functools
from collections.abc import Callable
from typing import ParamSpec, TypeVar, cast

P = ParamSpec("P")
R = TypeVar("R")


def cache(func: Callable[P, R]) -> Callable[P, R]:
    """Decorate a function with @functools.cache without losing its signature."""

    @functools.wraps(func)
    @functools.cache
    def _wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        return func(*args, **kwargs)

    return cast(Callable[P, R], _wrapper)


def lru_cache(
    maxsize: int, typed: bool = False  # noqa: FBT001 FBT002
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """Decorate a function with @functools.lru_cache without losing its signature."""

    def _decorator(func: Callable[P, R]) -> Callable[P, R]:
        @functools.wraps(func)
        @functools.lru_cache(maxsize=maxsize, typed=typed)
        def _wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            return func(*args, **kwargs)

        return cast(Callable[P, R], _wrapper)

    return _decorator
