#!/usr/bin/env python
"""
Followuptasks.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : followuptasks
# @created     : Monday Nov 20, 2023 09:31:13 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of submitting follow-up tasks
from time import sleep
from secrets import randbelow
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import as_completed


def task1():
    """mock test that works for moment"""
    value = randbelow(10) / 10.0
    sleep(value)
    print(f"Task 1: {value}", flush=True)
    return value


def task2(value1):
    """mock test that works for moment"""
    value2 = randbelow(10) / 10.0
    sleep(value2)
    print(f"Task 2: value1={value1}, value2={value2}", flush=True)
    return value2


def main():
    """entry point"""
    # start the process pool
    with ProcessPoolExecutor(4) as executor:
        # send in the first tasks
        futures1 = [executor.submit(task1) for _ in range(10)]
        # process results in the order they are completed
        with ProcessPoolExecutor(2) as flexecutor:
            for future1 in as_completed(futures1):
                # get the result
                result = future1.result()
                # check if we should trigger a follow-up task
                if result > 0.5:
                    flexecutor.submit(task2, result)
        # wait for all follow-up tasks to complete


if __name__ == "__main__":
    main()
