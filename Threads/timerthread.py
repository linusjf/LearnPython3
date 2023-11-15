#!/usr/bin/env python
"""
Timerthread.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : timerthread
# @created     : Wednesday Nov 15, 2023 11:58:06 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of using a thread timer object
from threading import Timer
from secrets import randbelow


def task(message, timeout):
    """# target task function"""
    # report the custom message
    print(f"After {timeout} second(s), {message}")


# create a thread timer object
tm = randbelow(10)
timer = Timer(tm, task, args=('Hello, world!', tm))
# start the timer object
timer.start()
# wait for the timer to finish
print('Waiting for the timer...')
