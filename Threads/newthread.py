#!/usr/bin/env python
"""
Newthread.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : newthread
# @created     : Monday Nov 13, 2023 05:25:39 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of running a function in another thread
from time import sleep
from threading import Thread


def task():
    """Define task."""
    # block for a moment
    sleep(1)
    # display a message
    print('This is from another thread')


# create a thread
thread = Thread(target=task)
# run the thread
thread.start()
# wait for the thread to finish
print('Waiting for the thread...')
thread.join()
