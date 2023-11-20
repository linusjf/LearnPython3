#!/usr/bin/env python
"""
Unflushedprint.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : unflushedprint
# @created     : Monday Nov 20, 2023 03:32:50 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of not flushing output when call print() from tasks in new processes
from time import sleep
from multiprocessing import get_context
from concurrent.futures import ProcessPoolExecutor


def task(value):
    """custom task that will sleep for a moment"""
    sleep(value)
    print(f'Done: {value}')


def main():
    """entry point"""
    # create a start process context
    context = get_context('spawn')
    # start the process pool
    with ProcessPoolExecutor(mp_context=context) as executor:
        executor.map(task, range(5))
    print('All done!')
    with ProcessPoolExecutor() as executor:
        executor.map(task, range(5))
    print('All done!')


if __name__ == '__main__':
    main()
