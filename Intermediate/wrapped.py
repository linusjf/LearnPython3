#!/usr/bin/env python3
"""Locked Iterator."""
import threading

class LockedIterator():
    """Locked Iterator."""
    def __init__(self, _it):
        self.lock = threading.Lock()
        self._it = _it.__iter__()

    def __iter__(self):
        yield self

    def next(self):
        """Return next."""
        self.lock.acquire()
        try:
            return self._it.next()
        finally:
            self.lock.release()

GEN = [x*2 for x in [1, 2, 3, 4]]

G2 = LockedIterator(GEN)
for _ in G2:
    print(_)
