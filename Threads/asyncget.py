#!/usr/bin/env python
"""
Asyncget.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : asyncget
# @created     : Monday Nov 27, 2023 12:10:33 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of issuing a task with apply_async() to the thread pool and wait
# for the result
from secrets import randbelow
from time import sleep
from multiprocessing.pool import ThreadPool


def task():
    """task executed in a worker thread"""
    # generate a random value
    _value = randbelow(10) / 10.0
    # report a message
    print(f'Task generated {_value}')
    # block for a moment
    sleep(1)
    # report a message
    print(f'Task done with {_value}')
    # return the generated value
    return _value


# protect the entry point
if __name__ == '__main__':
    # create and configure the thread pool
    pool = ThreadPool()
    # issue tasks to the thread pool
    result = pool.apply_async(task)
    # wait for the return value
    value = result.get()
    # report the return value
    print(f'Got: {value}')
    # close the thread pool
    pool.close()
