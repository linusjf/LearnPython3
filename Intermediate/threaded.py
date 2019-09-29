#!/usr/bin/env python3
"""Threading generators and iterators."""
import threading
from collections.abc import Iterator

# pylint: disable=too-few-public-methods


class Counter(Iterator):
    """Counter class."""

    def __init__(self):
        """Initialise object."""
        self.i = 0
        # create a lock
        self.lock = threading.Lock()

    def __next__(self):
        """Return next."""
        # acquire/release the lock when updating self.i
        with self.lock:
            self.i += 1
            return self.i

# pylint: enable=too-few-public-methods


def loop(_func, _n):
    """Run the given function n times in a loop."""
    for _ in range(_n):
        _func()


def run(_f, repeats=1000, nthreads=10):
    """
    Start multiple threads.

    Execute the given function multiple
    times in each thread.
    """
    # create threads
    threads = [threading.Thread(target=loop, args=(_f, repeats))
               for i in range(nthreads)]

    # start threads
    for _t in threads:
        _t.start()

    # wait for threads to finish
    for _t in threads:
        _t.join()


def main():
    """Execute main."""
    _c2 = Counter()

    # call c2.next 100K times in 2 different threads
    run(_c2.__next__, repeats=100000, nthreads=2)
    print("c2: " + str(_c2.__next__()))


if __name__ == "__main__":
    main()
