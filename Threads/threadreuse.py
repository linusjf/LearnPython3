#!/usr/bin/env python
"""
Threadreuse.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : threadreuse
# @created     : Friday Nov 24, 2023 08:48:31 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of idle threads being reused for new tasks
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import wait
from time import sleep
import threading


def task():
    """task executed in the thread pool"""
    # block for a moment
    sleep(1)


# create the thread pool
with ThreadPoolExecutor(4) as tpe:
    # issue two tasks
    futures = [tpe.submit(task) for _ in range(2)]
    # wait for the tasks to complete
    _ = wait(futures)
    # report all running threads
    print('Running threads:')
    for thread in threading.enumerate():
        print(f'\t{thread}')
    # issue one task
    futures = [tpe.submit(task)]
    # wait for the task to complete
    _ = wait(futures)
    # report all running threads
    print('Running threads:')
    for thread in threading.enumerate():
        print(f'\t{thread}')
