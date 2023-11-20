#!/usr/bin/env python
"""
Mutexlock.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : mutexlock
# @created     : Monday Nov 20, 2023 14:21:41 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of a mutual exclusion (mutex) lock for processes
from time import sleep
from secrets import randbelow
from multiprocessing import Process
from multiprocessing import Lock


def task(_lock, identifier, value):
    """work function"""
    # acquire the lock
    with _lock:
        print(f">process {identifier} got the lock, sleeping for {value}")
        sleep(value)


# entry point
if __name__ == "__main__":
    # create the shared lock
    lock = Lock()
    # create a number of processes with different sleep times
    processes = [Process(target=task, args=(lock, i, randbelow(10))) for i in range(10)]
    # start the processes
    for process in processes:
        process.start()
    # wait for all processes to finish
    for process in processes:
        process.join()
