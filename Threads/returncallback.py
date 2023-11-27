#!/usr/bin/env python
"""
Returncallback.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : returncallback
# @created     : Monday Nov 27, 2023 12:02:04 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of issuing a task with apply_async() to the thread pool with
# a callback
from secrets import randbelow
from time import sleep
from multiprocessing.pool import ThreadPool


def return_callback(result):
    """handle the return value callback"""
    print(f'Callback received: {result}')


def task():
    """task executed in a worker thread"""
    # generate a random value
    value = randbelow(10) / 10.0
    # report a message
    print(f'Task generated {value}')
    # block for a moment
    sleep(1)
    # report a message
    print(f'Task done with {value}')
    # return the generated value
    return value


# protect the entry point
if __name__ == '__main__':
    # create and configure the thread pool
    pool = ThreadPool()
    # issue tasks to the thread pool
    pool.apply_async(task, callback=return_callback)
    # close the thread pool
    pool.close()
    # wait for all tasks to finish
    pool.join()
