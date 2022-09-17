# -*- coding: utf-8 -*-
import functools
import logging
import time

__all__ = ["Timer", "time_it"]


class Timer:
    def __init__(self) -> None:
        self._tic: float = 0
        self._toc: float = 0

        self._active: bool = False

    def start(self) -> "Timer":
        self._tic, self._toc = time.perf_counter(), 0
        self._active = True
        return self

    def stop(self) -> None:
        self._toc = time.perf_counter()
        self._active = False

    @property
    def active(self) -> bool:
        return self._active

    @property
    def elapsed(self) -> float:
        if self._active:
            return time.perf_counter() - self._tic

        return self._toc - self._tic

    def __enter__(self) -> "Timer":
        return self.start()

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.stop()

    def __str__(self) -> str:
        elapsed = self.elapsed
        return f"{elapsed :.3f}s" if elapsed >= 1.0 else f"{elapsed :.3f}ms"


def time_it(logger: logging.Logger = None, level: int = logging.DEBUG):
    _logger = logger or logging.getLogger("pytime.Timer")
    _timer = Timer()

    def decorator(func: callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with _timer:
                ret = func(*args, **kwargs)

            _logger.log(level, f"{func.__name__}():{_timer}")
            return ret

        return wrapper

    return decorator
