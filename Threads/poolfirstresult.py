#!/usr/bin/env python
"""
Poolfirstresult.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : poolfirstresult
# @created     : Tuesday Nov 28, 2023 05:22:41 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of the imap_unordered and wait for first result usage pattern
from time import sleep
from secrets import randbelow
from multiprocessing.pool import ThreadPool


def task(value):
    """task to execute in a new thread"""
    # generate a random value
    random_value = randbelow(100) / 100.0
    # block for moment
    sleep(random_value)
    # return result
    return (value, random_value)


# protect the entry point
if __name__ == '__main__':
    # create the thread pool
    with ThreadPool() as pool:
        # issue tasks and handle results
        it = pool.imap_unordered(task, range(10))
        # get the result from the first task to complete
        result = next(it)
        # report first result
        print(f'>got {result}')
