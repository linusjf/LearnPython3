#!/usr/bin/env python
"""
Norestart.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : norestart
# @created     : Thursday Nov 16, 2023 05:43:05 IST
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
# try and start the thread again
thread.start()
