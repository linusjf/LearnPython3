#!/usr/bin/env python
"""
Customthread.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : customthread
# @created     : Monday Nov 13, 2023 10:51:38 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of extending the Thread class
from time import sleep
from threading import Thread


class CustomThread(Thread):
    """Custom thread class"""
    def run(self):
        """Override the run function"""
        # block for a moment
        sleep(1)
        # display a message
        print('This is coming from another thread')


# create the thread
thread = CustomThread()
# start the thread
thread.start()
# wait for the thread to finish
print('Waiting for the thread to finish')
thread.join()
