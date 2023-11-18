#!/usr/bin/env python
"""
Threadinitexception.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : threadinitexception
# @created     : Saturday Nov 18, 2023 13:27:15 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of an exception in a thread pool initializer function
from time import sleep
from secrets import randbelow
from concurrent.futures import ThreadPoolExecutor


def initializer_worker():
    """function for initializing the worker thread"""
    # raise an exception
    raise Exception('Something bad happened!')


def task(identifier):
    """a mock task that sleeps for a random amount of time
    less than one second
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
