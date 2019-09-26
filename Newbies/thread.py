#!/usr/bin/env python3
"""Threading example."""
import time
import threading


class ThreadTester(threading.Thread):
    """Thread Tester class."""

    def __init__(self, identifier, name, i):
        """Construct the instance."""
        threading.Thread.__init__(self)
        self._id = identifier
        self.name = name
        self.i = i

    def run(self):
        """Run the thread."""
        thread_test(self.name, self.i, 5)
        print("%s has finished execution " % self.name)


def thread_test(name, wait, i):
    """Test a thread."""
    while i:
        time.sleep(wait)
        print("Running %s \n" % name)
        i = i - 1


if __name__ == "__main__":
    THREAD1 = ThreadTester(1, "First Thread", 1)
    THREAD2 = ThreadTester(2, "Second Thread", 2)
    THREAD3 = ThreadTester(3, "Third Thread", 3)

    THREAD1.start()
    THREAD2.start()
    THREAD3.start()

    THREAD1.join()
    THREAD2.join()
    THREAD3.join()
