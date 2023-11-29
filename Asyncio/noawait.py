#!/usr/bin/env python
"""
Noawait.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : noawait
# @created     : Wednesday Nov 29, 2023 12:18:15 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of unawaited coroutines report a RuntimeWarning
import asyncio


async def task(value):
    """simple task that takes a moment"""
    # report a message
    print(f'Task is running, value={value}')
    # block a moment
    asyncio.sleep(2)  # forget to await
    # report a message
    print(f'Task is done, value={value}')


async def main():
    """main coroutine"""
    # execute and await the task
    await task(99)


# start the event loop
asyncio.run(main(), debug=False)
