#!/usr/bin/env python
"""
Threadlocal.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : threadlocal
# @created     : Monday Nov 13, 2023 19:49:11 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of thread local storage
from time import sleep
import threading


def task(value):
    """# custom target function"""
    # create a local storage
    local = threading.local()
    # store data
    local.value = value
    # block for a moment
    sleep(value)
    # retrieve value
    print(f'Stored value: {local.value}')


# create and start a thread
threading.Thread(target=task, args=(1,)).start()
# create and start another thread
threading.Thread(target=task, args=(2,)).start()
