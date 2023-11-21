#!/usr/bin/env python
"""
Genroots.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : genroots
# @created     : Tuesday Nov 21, 2023 12:04:58 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import asyncio


async def py35_coro():
    """Native coroutine, modern syntax"""
    stf = await stuff()
    return stf


async def stuff():
    """Return stuff."""
    return 0x10, 0x20, 0x30


def gen():
    """Generator."""
    yield 0x10, 0x20, 0x30


async def main():
    """Main."""
    print(py35_coro())
    nums = await py35_coro()
    print(nums)
    genr = gen()
    # Nothing much happens - need to iterate with `.__next__()`
    print(genr)
    print(next(genr))


if __name__ == "__main__":
    asyncio.run(main())
