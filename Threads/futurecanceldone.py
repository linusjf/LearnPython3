#!/usr/bin/env python
"""
Futurecanceldone.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : futurecanceldone
# @created     : Friday Nov 17, 2023 20:40:09 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of trying to cancel a done task via its future
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import wait


def work(sleep_time):
    """mock task that will sleep for a moment"""
    sleep(sleep_time)


# create a thread pool
with ThreadPoolExecutor(1) as executor:
    # start a long running task
    future = executor.submit(work, 2)
    running = future.running()
    # wait for the task to finish
    wait([future])
    # check the status
    running = future.running()
    cancelled = future.cancelled()
    done = future.done()
    print(f'Task running={running}, cancelled={cancelled}, done={done}')
    # try to cancel the task
    WAS_CANCELLED = future.cancel()
    print(f'Task was cancelled: {WAS_CANCELLED}')
    # check if it was cancelled
    running = future.running()
    cancelled = future.cancelled()
    done = future.done()
    print(f'Task running={running}, cancelled={cancelled}, done={done}')
