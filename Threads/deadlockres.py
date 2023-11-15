#!/usr/bin/env python
"""
Deadlock2.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : deadlock2
# @created     : Wednesday Nov 15, 2023 18:48:17 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of a deadlock caused by a thread waiting on itself
from threading import Thread
from threading import RLock


def task2(_lock):
    """# task2 to be executed in a new thread"""
    print('Thread acquiring lock again...')
    with _lock:
        # will never get here
        pass


def task1(_lock):
    """# task1 to be executed in a new thread"""
    print('Thread acquiring lock...')
    with _lock:
        task2(_lock)


# create the mutex lock
lock = RLock()
# create and configure the new thread
thread = Thread(target=task1, args=(lock,))
# start the new thread
thread.start()
# wait for threads to exit...
thread.join()
