#!/usr/bin/env python
"""
Howlong.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : howlong
# @created     : Wednesday Nov 29, 2023 11:48:33 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of configuring slow_callback_duration in debug mode
import logging
import time
import asyncio


async def task(value):
    """simple task that takes a moment"""
    # report a message
    print(f'Task is running, value={value}')
    # block a moment
    time.sleep(0.012)
    # report a message
    print(f'Task is done, value={value}')


async def main():
    """main coroutine"""
    # change the how long limit for reporting warnings
    loop = asyncio.get_running_loop()
    loop.slow_callback_duration = 0.01  # 10 ms
    # execute and await the task
    await task(99)


# enable debug logging
logging.basicConfig(level=logging.DEBUG)
# start the event loop
asyncio.run(main(), debug=True)
