#!/usr/bin/env python
"""
Taskcount.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : taskcount
# @created     : Monday Nov 20, 2023 09:46:15 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of estimating the number of remaining tasks
from time import sleep
from secrets import randbelow
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import as_completed


def task():
    """mock test that works for moment"""
    value = randbelow(100) / 100.0
    sleep(value)


def main():
    """entry point"""
    # start the process pool
    with ProcessPoolExecutor(4) as executor:
        # submit many tasks
        futures = [executor.submit(task) for _ in range(50)]
        print('Waiting for tasks to complete...')
        # update each time a task finishes
        for _ in as_completed(futures):
            # report the number of remaining tasks
            items = executor._pending_work_items  # pylint: disable=protected-access
            print(f'About {len(items)} tasks remain')


if __name__ == '__main__':
    main()
