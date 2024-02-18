# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2024 Michał Góral.

import sys
import atexit
import itertools
from threading import RLock
from contextlib import contextmanager


# Rough idea for function registry stolen from weakref.finalize implementation
class cleanup:
    __slots__ = ()
    _index_iter = itertools.count()
    _registry = {}
    _is_atexit = False
    lock = RLock()

    class _Info:
        __slots__ = ("fn", "args", "kwargs", "index")

    def __init__(self, fn, *args, **kwargs):
        if not self._is_atexit:
            atexit.register(self.run_all)
            cleanup._is_atexit = True

        info = self._Info()
        info.fn = fn
        info.args = args
        info.kwargs = kwargs
        info.index = next(self._index_iter)
        with self.lock:
            self._registry[self] = info

    def __call__(self):
        with self.lock:
            info = self._registry.pop(self, None)
        if info:
            return info.fn(*info.args, **info.kwargs)
        return None

    def cancel(self):
        with self.lock:
            self._registry.pop(self, None)

    @classmethod
    @contextmanager
    def clean_on_exit(cls):
        try:
            yield
        finally:
            cls.run_all()

    @classmethod
    def run_all(cls):
        try:
            # theoretically cleanup actions may create new cleanups by
            # themselves, so we must handle this in an infinite loop
            while True:
                cleanups = cls._get_cleanups()
                if not cleanups:
                    break

                cl = cleanups.pop()
                try:
                    cl()
                except Exception:
                    sys.excepthook(*sys.exc_info())  # show exception on stderr

            with cls.lock:
                assert len(cls._registry) == 0
        finally:
            atexit.unregister(cls.run_all)
            cls._is_atexit = False

    @classmethod
    def _get_cleanups(cls):
        with cls.lock:
            lst = list(cls._registry.items())
        lst.sort(key=lambda elem: elem[1].index)  # oldest last, but we use list.pop
        return [cl for cl, _ in lst]  # force retrieval of info via cleanup object
