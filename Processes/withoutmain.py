#!/usr/bin/env python
"""
Withoutmain.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : withoutmain
# @created     : Sunday Nov 19, 2023 21:46:00 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of not having a check for the main top-level environment
from multiprocessing import get_context
from time import sleep
from secrets import randbelow
from concurrent.futures import ProcessPoolExecutor


def task(value):
    """custom task that will sleep for a variable amount of time"""
    # sleep for less than a second
    sleep(randbelow(10) / 10.0)
    return value


# create a start process context
context = get_context("spawn")
# start the process pool
with ProcessPoolExecutor(mp_context=context) as executor:
    # submit all tasks
    for result in executor.map(task, range(5)):
        print(result)
