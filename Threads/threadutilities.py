#!/usr/bin/env python
"""
Threadutilities.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : threadutilities
# @created     : Monday Nov 13, 2023 16:02:41 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# report the number of active threads
from threading import active_count
from threading import Thread
from threading import current_thread
from threading import get_ident
from threading import get_native_id
import threading
# get the number of active threads
COUNT = active_count()
# report the number of active threads
print(COUNT)

# SuperFastPython.com
# retrieve the current thread within


def task():
    """# function to get the current thread"""
    # get the current thread
    curr = current_thread()
    # report the name
    print(curr.name)


# create a thread
thread = Thread(target=task)
# start the thread
thread.start()
# wait for the thread to exit
thread.join()

# SuperFastPython.com
# report the id for the current thread
# get the id for the current thread
identifier = get_ident()
# report the thread id
print(identifier)

# SuperFastPython.com
# report the native id for the current thread
# get the native id for the current thread
identifier = get_native_id()
# report the thread id
print(identifier)

# SuperFastPython.com
# enumerate all active threads
# get a list of all active threads
threads = threading.enumerate()
# report the name of all active threads
for thread in threads:
    print(thread.name)
