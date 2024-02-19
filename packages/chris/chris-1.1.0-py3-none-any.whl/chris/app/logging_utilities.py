"""Logging utilities."""

import functools
import time
from typing import Callable, TypeVar
from typing_extensions import ParamSpec

from fastapi.logger import logger

P = ParamSpec("P")  # Parameter type variable for decorated function
R = TypeVar("R")  # Return type variable for decorated function

DEFAULT_LOG_SIZE = 5000000
DEFAULT_N_BACKUPS = 5


def log_context(name: str, tag: str = "=") -> Callable[[Callable[P, R]], Callable[P, R]]:
    """
    Decorate a function for logging activity.

    :param name: Name of the activity.
    :param tag: Tag for the kind of activity.
    """

    def decorator(decorated_func: Callable[P, R]) -> Callable[P, R]:

        @functools.wraps(decorated_func)
        def func_wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            start_time = time.time()
            logger.info(f"[{tag}] Start:{name}")
            result = decorated_func(*args, **kwargs)
            total_time = round(time.time() - start_time, 5)
            logger.info(f"[{tag}] End:{name}, Time:{total_time}")
            return result

        return func_wrapper

    return decorator
