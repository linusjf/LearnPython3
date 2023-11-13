#!/usr/bin/env python
"""
Threadswithargs.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : threadswithargs
# @created     : Monday Nov 13, 2023 05:44:22 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of running a function with arguments in another thread
from time import sleep
from threading import Thread


def task(sleep_time, message):
    """a custom function that blocks for a moment"""
    # block for a moment
    sleep(sleep_time)
    # display a message
    print(message)


# create a thread
thread = Thread(target=task, args=(1.5, 'New message from another thread'))
# run the thread
thread.start()
# wait for the thread to finish
print('Waiting for the thread...')
thread.join()
