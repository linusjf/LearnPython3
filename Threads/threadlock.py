#!/usr/bin/env python
"""
Threadlock.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : threadlock
# @created     : Tuesday Nov 14, 2023 13:49:01 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of a mutual exclusion (mutex) lock
from time import sleep
from secrets import randbelow
from threading import Thread
from threading import Lock


def task(lock_, identifier, value):
    """# work function"""
    # acquire the lock
    with lock_:
        print(f'>thread {identifier} got the lock, sleeping for {value}')
        sleep(value)


# create a shared lock
lock = Lock()
# start a few threads that attempt to execute the same critical section
for i in range(10):
    # start a thread
    Thread(target=task, args=(lock, i, randbelow(10))).start()
# wait for all threads to finish...
