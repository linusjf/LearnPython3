#!/usr/bin/env python3
"""Threading generators and iterators."""
from threading import Lock
from threading import Thread
from collections.abc import Iterator

# pylint: disable=too-few-public-methods
class ThreadSafeIter(Iterator):
    """Takes an iterator/generator and makes it thread-safe by
    serializing call to the `next` method of given iterator/generator.
    """
    def __init__(self, iterator):
        self._it = iterator.__iter__()
        self.lock = Lock()

    def __next__(self):
        with self.lock:
            return self._it.__next__()
# pylint: enable=too-few-public-methods

def threadsafe_generator(_f):
    """A decorator that takes a generator function and makes it thread-safe.
    """
    def gen(*_a, **_kw):
        return ThreadSafeIter(_f(*_a, **_kw))
    return gen

@threadsafe_generator
def count():
    """Generate count."""
    i = 0
    while True:
        i += 1
        yield i

# pylint: disable=too-few-public-methods
class Counter(Iterator):
    """Counter class."""

    def __init__(self):
        """Initialise object."""
        self.i = 0
        # create a lock
        self.lock = Lock()

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
    threads = [Thread(target=loop, args=(_f, repeats))
               for i in range(nthreads)]

    # start threads
    for _t in threads:
        _t.start()

    # wait for threads to finish
    for _t in threads:
        _t.join()


def main():
    """Execute main."""
    _c1 = count()
    # _c1 = ThreadSafeIter(_c1)
    _c2 = Counter()

    run(_c1.__next__, repeats=100000, nthreads=2)
    print("c1: " + str(_c1.__next__()))
    # call c2.next 100K times in 2 different threads
    run(_c2.__next__, repeats=100000, nthreads=2)
    print("c2: " + str(_c2.__next__()))


if __name__ == "__main__":
    main()
