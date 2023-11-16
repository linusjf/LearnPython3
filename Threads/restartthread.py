#!/usr/bin/env python
"""
Restartthread.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : restartthread
# @created     : Thursday Nov 16, 2023 05:47:46 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of reusing a thread
from time import sleep
from threading import Thread


def task():
    """# custom target function"""
    # block for a moment
    sleep(1)
    # report a message
    print('Hello, from the new thread')


# create a new thread
thread = Thread(target=task)
# start the thread
thread.start()
# wait for the thread to finish
thread.join()
# create a new thread with the same config
thread2 = Thread(target=task)
# start the new thread
thread2.start()
# wait for the new thread to finish
thread2.join()
