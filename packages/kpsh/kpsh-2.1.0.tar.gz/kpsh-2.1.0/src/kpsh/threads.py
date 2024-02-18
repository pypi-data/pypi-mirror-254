# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2024 Michał Góral.

"""This implements a thread pool which makes sure that only one thread with
a specific name exists at a time. When user asks to create a second thread,
the previous one is cancelled (when possible) and joined before starting
the new one."""

from typing import Optional
import threading


def run(name: str, fn, args=None, kwargs=None) -> threading.Thread:
    t = threading.Thread(target=fn, args=args, kwargs=kwargs)
    return _run(name, t)


def run_later(name: str, interval: int, fn, args=None, kwargs=None) -> threading.Thread:
    t = threading.Timer(interval, function=fn, args=args, kwargs=kwargs)
    return _run(name, t)


def find_thread(name: str) -> Optional[threading.Thread]:
    for t in threading.enumerate():
        if t.name == name:
            return t
    return None


def stop():
    mt = threading.main_thread()
    ct = threading.current_thread()
    for t in threading.enumerate():
        if t not in (mt, ct):
            _stop_thread(t)


def _stop_thread(thread: threading.Thread):
    if hasattr(thread, "cancel"):
        thread.cancel()
    thread.join()


def _run(name, thread: threading.Thread) -> threading.Thread:
    old = find_thread(name)
    if old:
        _stop_thread(old)

    thread.name = name
    thread.start()
    return thread
