#!/usr/bin/env python3
"""LockedIterator."""
from threading import Lock
from collections.abc import Iterator

# pylint: disable=too-few-public-methods


class LockedIterator(Iterator):
    """Locked Iterator."""

    def __init__(self, _it):
        """Initialise object."""
        self.lock = Lock()
        self._it = _it.__iter__()

    def __next__(self):
        """Return next."""
        self.lock.acquire()
        try:
            return self._it.__next__()
        finally:
            self.lock.release()

    def send(self, msg):
        """Send message."""
        self.lock.acquire()
        try:
            self._it.send(msg)
        except StopIteration as _si:
            print(_si)
        finally:
            self.lock.release()


# pylint: enable=too-few-public-methods
