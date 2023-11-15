#!/usr/bin/env python
"""
Semaphore.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : semaphore
# @created     : Wednesday Nov 15, 2023 08:40:10 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of using a semaphore
from time import sleep
from secrets import randbelow
from threading import Thread
from threading import Semaphore


def task(_semaphore, number):
    """# target function"""
    # attempt to acquire the semaphore
    with _semaphore:
        # process
        value = randbelow(3)
        sleep(value)
        # report result
        print(f'Thread {number} got {value}')


# create a semaphore
semaphore = Semaphore(2)
# create a suite of threads
for i in range(10):
    worker = Thread(target=task, args=(semaphore, i))
    worker.start()
# wait for all workers to complete...
