#!/usr/bin/env python
"""
Longtask.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : longtask
# @created     : Wednesday Nov 29, 2023 11:45:21 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of task took too long in debug mode with warnings
import warnings
import time
import asyncio


async def task(value):
    """simple task that takes a moment"""
    # report a message
    print(f'Task is running, value={value}')
    # block a moment
    time.sleep(2)
    # report a message
    print(f'Task is done, value={value}')


async def main():
    """main coroutine"""
    # execute and await the task
    await task(99)


# enable all warnings
warnings.simplefilter('always')
# start the event loop
asyncio.run(main(), debug=True)
