#!/usr/bin/env python
"""
Configthreadpool.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : configthreadpool
# @created     : Friday Nov 17, 2023 15:00:49 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# report the default number of worker threads on your system
from concurrent.futures import ThreadPoolExecutor
from threading import main_thread
import threading
# create a thread pool with the default number of worker threads
pool = ThreadPoolExecutor()
# report the number of worker threads chosen by default
print(pool._max_workers)  # pylint: disable=protected-access
# create a thread pool with a large number of worker threads
pool = ThreadPoolExecutor(500)
# report the number of worker threads
print(pool._max_workers)  # pylint: disable=protected-access

# access the name of the main thread
thread = main_thread()
# report the thread name
print(thread.name)


# report the default name of threads in the thread pool
def task(_):
    """a mock task that does nothing"""
    pass  # pylint: disable=unnecessary-pass


# create a thread pool
executor = ThreadPoolExecutor()
# execute asks
executor.map(task, range(10))
# report all thread names
for thread in threading.enumerate():
    print(thread.name)
# shutdown the thread pool
executor.shutdown()

# create a thread pool with a custom name prefix
executor = ThreadPoolExecutor(thread_name_prefix='TaskPool')
# execute asks
executor.map(task, range(10))
# report all thread names
for thread in threading.enumerate():
    print(thread.name)
# shutdown the thread pool
executor.shutdown()
