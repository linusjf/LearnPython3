#!/usr/bin/env python
"""
Mapexception.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : mapexception
# @created     : Saturday Nov 18, 2023 14:46:39 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of handling an exception raised within a task
from time import sleep
from concurrent.futures import ThreadPoolExecutor


def work(_):
    """mock task that will sleep for a moment"""
    sleep(1)
    raise Exception('Something bad happened!')


# create a thread pool
with ThreadPoolExecutor() as executor:
    # execute our task
    for result in executor.map(work, [1]):
        print(result)
