#!/usr/bin/env python
"""
Poolimap.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : poolimap
# @created     : Monday Nov 27, 2023 18:02:35 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of parallel imap() with the thread pool
from secrets import randbelow
from time import sleep
from multiprocessing.pool import ThreadPool


def task(identifier):
    """task executed in a worker thread"""
    # generate a value
    value = randbelow(10000) / 10000.0
    # report a message
    print(f'Task {identifier} executing with {value}')
    # block for a moment
    sleep(value)
    # return the generated value
    return value


# protect the entry point
if __name__ == '__main__':
    # create and configure the thread pool
    with ThreadPool() as pool:
        # execute tasks in order
        for result in pool.imap(task, range(50)):
            print(f'Got result: {result}')
    # thread pool is closed automatically
