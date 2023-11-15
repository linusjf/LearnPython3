#!/usr/bin/env python
"""
Barrier.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : barrier
# @created     : Wednesday Nov 15, 2023 12:13:43 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of using a barrier
from time import sleep
from secrets import randbelow
from threading import Thread
from threading import Barrier


def task(_barrier, number):
    """# target function to prepare some work"""
    # generate a unique value
    value = randbelow(5)
    # block for a moment
    sleep(value)
    # report result
    print(f'Thread {number} done, got: {value}')
    # wait on all other threads to complete
    _barrier.wait()


# create a barrier
barrier = Barrier(5 + 1)
# create the worker threads
for i in range(5):
    # start a new thread to perform some work
    worker = Thread(target=task, args=(barrier, i))
    worker.start()
# wait for all threads to finish
print('Main thread waiting on all results...')
barrier.wait()
# report once all threads are done
print('All threads have their result')
