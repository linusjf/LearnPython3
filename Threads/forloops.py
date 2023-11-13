#!/usr/bin/env python
"""
Forloops.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : forloops
# @created     : Monday Nov 13, 2023 15:36:09 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of a parallel for loop with the Thread class
from threading import Thread
from time import sleep
from secrets import randbelow


def task(value):
    """# execute a task"""
    # add your work here...
    sleep(randbelow(20))
    # ...
    # all done
    print(f'.done {value}')


# protect the entry point
if __name__ == '__main__':
    # create all tasks
    threads = [Thread(target=task, args=(i,)) for i in range(20)]
    # start all threads
    for thread in threads:
        thread.start()
    # wait for all threads to complete
    for thread in threads:
        thread.join()
    # report that all tasks are completed
    print('Done')
