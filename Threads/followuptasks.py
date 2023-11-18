#!/usr/bin/env python
"""
Followuptasks.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : followuptasks
# @created     : Saturday Nov 18, 2023 18:35:50 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of submitting follow-up tasks
from time import sleep
from secrets import randbelow
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed


def task1():
    """mock test that works for moment"""
    value = randbelow(10) / 10.0
    sleep(value)
    print(f'Task 1: {value}')
    return value


def task2(value1):
    """mock test that works for moment"""
    value2 = randbelow(10) / 10.0
    sleep(value2)
    print(f'Task 2: value1={value1}, value2={value2}')
    return value2


# start the thread pool
with ThreadPoolExecutor(5) as executor:
    # send in the first tasks
    futures1 = [executor.submit(task1) for _ in range(10)]
    # process results in the order they are completed
    futures2 = []
    for future1 in as_completed(futures1):
        # get the result
        result = future1.result()
        # check if we should trigger a follow-up task
        if result > 0.5:
            future2 = executor.submit(task2, result)
            futures2.append(future2)
    # wait for all follow-up tasks to complete
