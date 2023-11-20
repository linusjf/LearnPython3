#!/usr/bin/env python
"""
Reentrantlock.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : reentrantlock
# @created     : Monday Nov 20, 2023 15:36:02 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of a reentrant lock for processes
from time import sleep
from secrets import randbelow
from multiprocessing import Process
from multiprocessing import RLock


def report(_lock, identifier):
    """Reporting function."""
    # acquire the lock
    with _lock:
        print(f'>process {identifier} done')


def task(_lock, identifier, value):
    """Work function."""
    # acquire the lock
    with _lock:
        print(f'>process {identifier} sleeping for {value}')
        sleep(value)
        # report
        report(lock, identifier)


# entry point
if __name__ == '__main__':
    # create a shared reentrant lock
    lock = RLock()
    # create processes
    processes = [Process(target=task, args=(lock, i, randbelow(5))) for i in range(10)]
    # start child processes
    for process in processes:
        process.start()
    # wait for child processes to finish
    for process in processes:
        process.join()
