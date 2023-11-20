#!/usr/bin/env python
"""
Stoptasks.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : stoptasks
# @created     : Monday Nov 20, 2023 09:18:22 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of stopping running tasks using an event
from time import sleep
from multiprocessing import Manager
from concurrent.futures import ProcessPoolExecutor


def work(event):
    """mock target task function"""
    # pretend read data for a long time
    for _ in range(100):
        # pretend to read some data
        sleep(1)
        # check the status of the flag
        if event.is_set():
            # shut down this task now
            print('Not done, asked to stop', flush=True)
            return None
    return "All done!"


def main():
    """entry point"""
    # create the manager to coordinate shared objects like the event
    with Manager() as manager:
        # create an event to shut down all running tasks
        event = manager.Event()
        # create a process pool
        executor = ProcessPoolExecutor()
        # execute all of our tasks
        futures = [executor.submit(work, event) for _ in range(50)]
        # wait a moment
        print('Tasks are running...')
        sleep(2)
        # cancel all scheduled tasks
        print('Cancelling all scheduled tasks...')
        for future in futures:
            future.cancel()
        # stop all currently running tasks
        print('Trigger all running tasks to stop...')
        event.set()
        # shutdown the process pool and wait for all tasks to complete
        print('Shutting down, waiting for all tasks...')
        executor.shutdown()


if __name__ == '__main__':
    main()
