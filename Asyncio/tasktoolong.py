#!/usr/bin/env python
"""
Tasktoolong.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : tasktoolong
# @created     : Wednesday Nov 29, 2023 11:41:26 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of task took too long in debug mode with logging
import logging
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


# enable debug logging
logging.basicConfig(level=logging.DEBUG)
# start the event loop
asyncio.run(main(), debug=True)
