#!/usr/bin/env python
"""
Unsafecounter.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : unsafecounter
# @created     : Tuesday Dec 05, 2023 13:38:18 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of a thread-unsafe counter (with race conditions)
from threading import Thread


class ThreadUnsafeCounter():
    """thread unsafe counter class"""
    # constructor
    def __init__(self):
        # initialize counter
        self._counter = 0

    def increment(self):
        """increment the counter"""
        self._counter += 1

    def value(self):
        """get the counter value"""
        return self._counter


def task(_counter):
    """task executed by threads"""
    # increment the counter
    for _ in range(1000000):
        _counter.increment()


# create the counter
counter = ThreadUnsafeCounter()
# create 10 threads to increment the counter
threads = [Thread(target=task, args=(counter,)) for _ in range(10)]
# start all threads
for thread in threads:
    thread.start()
# wait for all threads to finish
for thread in threads:
    thread.join()
# report the value of the counter
print(counter.value())
