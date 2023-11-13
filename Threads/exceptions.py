#!/usr/bin/env python
"""
Exceptions.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : exceptions
# @created     : Monday Nov 13, 2023 17:35:50 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of an unhandled exception in a thread
from time import sleep
from threading import Thread
import threading


def work():
    """# target function that raises an exception"""
    print('Working...')
    sleep(1)
    # rise an exception
    raise Exception('Something bad happened')


# create a thread
thread = Thread(target=work)
# run the thread
thread.start()
# wait for the thread to finish
thread.join()
# continue on
print('Continuing on...')

# SuperFastPython.com
# example of an unhandled exception in a thread


def custom_hook(args):
    """# custom exception hook"""
    # report the failure
    print(f'Thread failed: {args.exc_value}')


# set the exception hook
threading.excepthook = custom_hook
# create a thread
thread = threading.Thread(target=work)
# run the thread
thread.start()
# wait for the thread to finish
thread.join()
# continue on
print('Continuing on...')
