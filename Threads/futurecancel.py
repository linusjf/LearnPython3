#!/usr/bin/env python
"""
Futurecancel.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : futurecancel
# @created     : Friday Nov 17, 2023 20:32:05 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of cancelling a task via it's future
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import wait


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
    # cancel the second task
    WAS_CANCELLED = future2.cancel()
    print(f'Second task was cancelled: {WAS_CANCELLED}')
    # wait for the second task to finish, just in case
    wait([future2])
    # confirm it was cancelled
    running = future2.running()
    cancelled = future2.cancelled()
    done = future2.done()
    print(f'Second task running={running}, cancelled={cancelled}, done={done}')
    # wait for the long running task to finish
    wait([future1])
