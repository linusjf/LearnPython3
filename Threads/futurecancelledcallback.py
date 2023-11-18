#!/usr/bin/env python
"""
Futurecancelledcallback.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : futurecancelledcallback
# @created     : Saturday Nov 18, 2023 09:22:18 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of a callback for a cancelled task via the future object
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import wait


def custom_callback(_):
    """callback function to call when a task is completed"""
    print('Custom callback was called')


def work(sleep_time):
    """mock task that will sleep for a moment"""
    sleep(sleep_time)


# create a thread pool
with ThreadPoolExecutor(1) as executor:
    # start a long running task
    future1 = executor.submit(work, 2)
    running = future1.running()
    print(f'First task running={running}')
    # start a second
    future2 = executor.submit(work, 0.1)
    running = future2.running()
    print(f'Second task running={running}')
    # add the custom callback
    future2.add_done_callback(custom_callback)
    # cancel the second task
    WAS_CANCELLED = future2.cancel()
    print(f'Second task was cancelled: {WAS_CANCELLED}')
    # explicitly wait for all tasks to complete
    wait([future1, future2])
