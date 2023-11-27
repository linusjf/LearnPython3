#!/usr/bin/env python
"""
Poolmap.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : poolmap
# @created     : Monday Nov 27, 2023 13:51:03 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of parallel map() with the thread pool
from secrets import randbelow
from time import sleep
from multiprocessing.pool import ThreadPool


def task(identifier):
    """task executed in a worker thread"""
    # generate a value
    value = randbelow(10) / 10.0
    # report a message
    print(f'Task {identifier} executing with {value}')
    # block for a moment
    sleep(value)
    # return the generated value
    return value


def task2(identifier):
    """task executed in a worker thread"""
    # generate a value
    value = randbelow(10) / 10.0
    # report a message
    print(f'Task {identifier} executing with {value}')
    # block for a moment
    sleep(value)


# protect the entry point
if __name__ == '__main__':
    # create and configure the thread pool
    with ThreadPool() as pool:
        # execute tasks in order
        for result in pool.map(task, range(10)):
            print(f'Got result: {result}')
    # thread pool is closed automatically
    # create and configure the thread pool
    with ThreadPool() as pool:
        # execute tasks in order
        pool.map(task2, range(10))
