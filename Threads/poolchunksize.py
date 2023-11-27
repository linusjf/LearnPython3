#!/usr/bin/env python
"""
Poolchunksize.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : poolchunksize
# @created     : Monday Nov 27, 2023 13:59:19 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of parallel map() with the thread pool with a larger iterable
# and chunksize
from secrets import randbelow
from time import sleep
from multiprocessing.pool import ThreadPool
from threading import current_thread


def task(identifier):
    """task executed in a worker thread"""
    # generate a value
    value = randbelow(10) / 10.0
    # report a message
    print(f'Task {identifier} executing with {value} in thread: {current_thread().name}')
    # block for a moment
    sleep(1)
    # return the generated value
    return value


# protect the entry point
if __name__ == '__main__':
    # create and configure the thread pool
    with ThreadPool(4) as pool:
        # execute tasks in chunks, block until all complete
        pool.map(task, range(40), chunksize=10)
    # thread pool is closed automatically
