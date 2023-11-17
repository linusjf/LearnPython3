#!/usr/bin/env python
"""
Threadpool.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : threadpool
# @created     : Friday Nov 17, 2023 12:29:10 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of a parallel for loop with the ThreadPool class
from multiprocessing.pool import ThreadPool
from secrets import randbelow
from time import sleep


def task(value):
    """execute a task"""
    # add your work here...
    sleep(randbelow(3))
    # ...
    # return a result, if needed
    return value


# protect the entry point
if __name__ == '__main__':
    # create the pool with the default number of workers
    with ThreadPool() as pool:
        # issue one task for each call to the function
        for result in pool.map(task, range(100)):
            # handle the result
            print(f'>got {result}')
    # report that all tasks are completed
    print('Done')
