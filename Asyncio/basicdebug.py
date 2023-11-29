#!/usr/bin/env python
"""
Basicdebug.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : basicdebug
# @created     : Wednesday Nov 29, 2023 12:24:10 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of custom debug logging
import logging
import asyncio


async def task(value):
    """simple task that takes a moment"""
    # report a message
    logging.debug('Task is running, value=%s', value)
    # block a moment
    await asyncio.sleep(2)
    # report a message
    logging.debug('Task is done, value=%s', value)


async def main():
    """main coroutine"""
    # execute and await the task
    await task(99)


# enable debug logging
logging.basicConfig(level=logging.DEBUG)
# start the event loop
asyncio.run(main())
