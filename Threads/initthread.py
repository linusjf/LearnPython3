#!/usr/bin/env python
"""
Initthread.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : initthread
# @created     : Friday Nov 17, 2023 17:48:34 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of a custom worker thread initialization function
from time import sleep
from secrets import randbelow
from threading import current_thread
from concurrent.futures import ThreadPoolExecutor


def initializer_worker():
    """function for initializing the worker thread"""
    # get the unique name for this thread
    name = current_thread().name
    # store the unique worker name in a thread local variable
    print(f'Initializing worker thread {name}')


def task(identifier):
    """a mock task that sleeps for a random
    amount of time less than one second
    """
    sleep(randbelow(10) / 10.0)
    # get the unique name
    return identifier


# create a thread pool
with ThreadPoolExecutor(max_workers=2,
                        initializer=initializer_worker) as executor:
    # execute tasks
    for result in executor.map(task, range(10)):
        print(result)
