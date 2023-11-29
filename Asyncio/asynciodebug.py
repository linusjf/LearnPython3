#!/usr/bin/env python
"""
Asynciodebug.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : asynciodebug
# @created     : Wednesday Nov 29, 2023 11:15:18 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of enabling the asyncio module debugging
import logging
import asyncio


async def task(value):
    """simple task that takes a moment"""
    # report a message
    print(f'Task is running, value={value}')
    # block a moment
    await asyncio.sleep(2)
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
