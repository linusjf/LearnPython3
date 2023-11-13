#!/usr/bin/env python
"""
Valuedthread.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : valuedthread
# @created     : Monday Nov 13, 2023 11:40:00 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of extending the Thread class and return values
from time import sleep
from threading import Thread


class CustomThread(Thread):
    """# custom thread class"""

    def __init__(self):
        """Init"""
        super().__init__()
        self.value = 0

    def run(self):
        """# override the run function"""
        # block for a moment
        sleep(1)
        # display a message
        print('This is coming from another thread')
        # store return value
        self.value = 99


# create the thread
thread = CustomThread()
# start the thread
thread.start()
# wait for the thread to finish
print('Waiting for the thread to finish')
thread.join()
# get the value returned from run
VALUE = thread.value
print(f'Got: {VALUE}')
