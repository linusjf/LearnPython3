#!/usr/bin/env python
"""
Globaldata.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : globaldata
# @created     : Thursday Nov 16, 2023 14:22:28 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of returning a value from a thread
from time import sleep
from threading import Thread


def task():
    """function executed in a new thread"""
    # block for a moment
    sleep(1)
    # correctly scope the global variable
    global DATA  # pylint: disable=global-statement
    # store data in the global variable
    DATA = 'Hello from a new thread'


# define the global variable
DATA = None
# create a new thread
thread = Thread(target=task)
# start the thread
thread.start()
# wait for the thread to finish
thread.join()
# report the global variable
print(DATA)
