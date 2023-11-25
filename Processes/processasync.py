#!/usr/bin/env python
"""
Processasync.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : processasync
# @created     : Saturday Nov 25, 2023 07:49:15 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of a one-off asynchronous task with a process pool
from time import sleep
from multiprocessing.pool import Pool


def task():
    """function to execute in a new process"""
    # report a message
    print('Hello from the task', flush=True)
    # sleep a moment
    sleep(1)
    # report another message
    print('Task is all done', flush=True)


# entry point
if __name__ == '__main__':
    # create the process pool
    with Pool() as pool:
        # issue the task asynchronously
        async_result = pool.apply_async(task)
        # do other things, like report a message
        print('Main is doing other things...')
        # wait for the task to complete
        async_result.wait()
