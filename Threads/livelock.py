#!/usr/bin/env python
"""
Livelock.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : livelock
# @created     : Wednesday Nov 15, 2023 18:56:10 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of a livelock
from time import sleep
from threading import Thread
from threading import Lock


def task(number, _lock1, _lock2):
    """# task for worker threads"""
    # loop until the task is completed
    while True:
        # acquire the first lock
        with _lock1:
            # wait a moment
            sleep(0.1)
            # check if the second lock is available
            if _lock2.locked():
                print(f'Task {number} cannot get the second lock,giving up...')
            else:
                # acquire lock2
                with _lock2:
                    print(f'Task {number} made it, all done.')
                    break


# create locks
lock1 = Lock()
lock2 = Lock()
# create threads
thread1 = Thread(target=task, args=(0, lock1, lock2))
thread2 = Thread(target=task, args=(1, lock2, lock1))
# start threads
thread1.start()
thread2.start()
# wait for threads to finish
thread1.join()
thread2.join()
