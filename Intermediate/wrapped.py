#!/usr/bin/env python3
"""Locked Iterator."""
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

# pylint: enable=too-few-public-methods


GEN = [x * 2 for x in [1, 2, 3, 4]]

for _ in GEN:
    print(_)

G2 = LockedIterator(GEN)
for _ in G2:
    print(_)
