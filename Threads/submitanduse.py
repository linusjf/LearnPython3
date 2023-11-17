#!/usr/bin/env python
"""
Submitanduse.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : submitanduse
# @created     : Friday Nov 17, 2023 13:52:02 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of the submit and use as completed pattern for the ThreadPoolExecutor
from time import sleep
from secrets import randbelow
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from concurrent.futures import wait
from concurrent.futures import FIRST_COMPLETED


def task(name):
    """custom task that will sleep for a variable amount of time"""
    # sleep for less than a second
    sleep(randbelow(10) / 10.0)
    return name


# start the thread pool
with ThreadPoolExecutor(10) as executor:
    # submit tasks and collect futures
    futures = [executor.submit(task, i) for i in range(10)]
    # process task results as they are available
    for future in as_completed(futures):
        # retrieve the result
        print(future.result())

# start the thread pool
with ThreadPoolExecutor(10) as executor:
    # submit tasks and collect futures
    futures = [executor.submit(task, i) for i in range(10)]
    # process task results in the order they were submitted
    for future in futures:
        # retrieve the result
        print(future.result())


def custom_callback(fut):
    """custom callback function called on tasks when they complete"""
    # retrieve the result
    print(fut.result())


# start the thread pool
with ThreadPoolExecutor(10) as executor:
    # submit tasks and collect futures
    futures = [executor.submit(task, i) for i in range(10)]
    # register the callback on all tasks
    for future in futures:
        future.add_done_callback(custom_callback)
    # wait for tasks to complete...


def custom_callback1(fut):
    """custom callback function called on tasks when they complete"""
    # retrieve the result
    print(f'Callback 1: {fut.result()}')


def custom_callback2(fut):
    """custom callback function called on tasks when they complete"""
    # retrieve the result
    print(f'Callback 2: {fut.result()}')


# start the thread pool
with ThreadPoolExecutor(10) as executor:
    # submit tasks and collect futures
    futures = [executor.submit(task, i) for i in range(10)]
    # register the callbacks on all tasks
    for future in futures:
        future.add_done_callback(custom_callback1)
        future.add_done_callback(custom_callback2)
    # wait for tasks to complete...


# start the thread pool
with ThreadPoolExecutor(10) as executor:
    # submit tasks and collect futures
    futures = [executor.submit(task, i) for i in range(10)]
    # wait for all tasks to complete
    wait(futures)
    print('All tasks are done!')

# start the thread pool
with ThreadPoolExecutor(10) as executor:
    # submit tasks and collect futures
    futures = [executor.submit(task, i) for i in range(10)]
    # wait for all tasks to complete
print('All tasks are done!')

# start the thread pool
executor = ThreadPoolExecutor(10)
# submit tasks and collect futures
futures = [executor.submit(task, i) for i in range(10)]
# wait for all tasks to complete
executor.shutdown()
print('All tasks are done!')

# start the thread pool
executor = ThreadPoolExecutor(10)
# submit tasks and collect futures
futures = [executor.submit(task, i) for i in range(10)]
# wait until any task completes
done, not_done = wait(futures, return_when=FIRST_COMPLETED)
# get the result from the first task to complete
print(done.pop().result())
# shutdown without waiting
executor.shutdown(wait=False, cancel_futures=True)
