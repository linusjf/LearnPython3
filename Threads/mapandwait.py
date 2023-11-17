#!/usr/bin/env python
"""
Mapandwait.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : mapandwait
# @created     : Friday Nov 17, 2023 13:27:32 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of the map and wait pattern for the ThreadPoolExecutor
from time import sleep
from secrets import randbelow
from concurrent.futures import ThreadPoolExecutor


def task(name):
    """custom task that will sleep for a variable amount of time"""
    # sleep for less than a second
    sleep(randbelow(10) / 10.0)
    return name


# start the thread pool
with ThreadPoolExecutor(10) as executor:
    # execute tasks concurrently and process results in order
    for result in executor.map(task, range(10)):
        # retrieve the result
        print(result)


def tasktwo(value1, value2):
    """custom task that will sleep for a variable amount of time"""
    # sleep for less than a second
    sleep(randbelow(10) / 10.0)
    return (value1, value2)


# start the thread pool
with ThreadPoolExecutor() as executor:
    # submit all tasks
    for result in executor.map(tasktwo, ['1', '2', '3'], ['a', 'b', 'c']):
        print(result)


def taskthree(value):
    """custom task that will sleep for a variable amount of time"""
    # sleep for less than a second
    sleep(randbelow(10) / 10.0)
    print(f'Done: {value}')
    return value


# start the thread pool
with ThreadPoolExecutor() as executor:
    # submit all tasks
    executor.map(taskthree, range(5))
print('All done!')
