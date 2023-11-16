#!/usr/bin/env python
"""
Threadvalues.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : threadvalues
# @created     : Thursday Nov 16, 2023 14:17:39 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of returning multiple value from a thread
from time import sleep
from threading import Thread


class CustomThread(Thread):
    """custom thread"""
    def __init__(self):
        """constructor"""
        # execute the base constructor
        Thread.__init__(self)
        # set a default values
        self.value1 = None
        self.value2 = None
        self.value3 = None

    def run(self):
        """function executed in a new thread"""
        # block for a moment
        sleep(1)
        # store data in an instance variable
        self.value1 = 'Hello from a new thread'
        self.value2 = 99
        self.value3 = False


# create a new thread
thread = CustomThread()
# start the thread
thread.start()
# wait for the thread to finish
thread.join()
# report all values returned from a thread
print(thread.value1)
print(thread.value2)
print(thread.value3)
