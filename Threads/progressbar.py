#!/usr/bin/env python
"""
Progressbar.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : progressbar
# @created     : Sunday Nov 19, 2023 06:11:22 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of a simple progress indicator
from time import sleep
from secrets import randbelow
from concurrent.futures import ThreadPoolExecutor


def progress_indicator(_):
    """simple progress indicator callback function"""
    print('.', end='', flush=True)


def task():
    """mock test that works for moment"""
    sleep(randbelow(10) / 10.0)


# start the thread pool
with ThreadPoolExecutor(2) as executor:
    # send in the tasks
    futures = [executor.submit(task) for _ in range(20)]
    # register the progress indicator callback
    for future in futures:
        future.add_done_callback(progress_indicator)
    # wait for all tasks to complete
print('\nDone!')
