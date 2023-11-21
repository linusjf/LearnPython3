#!/usr/bin/env python
"""
Asyncgen.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : asyncgen
# @created     : Tuesday Nov 21, 2023 14:38:46 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import asyncio


async def mygen(num: int = 10):
    """Yield powers of 2."""
    i = 0
    while i < num:
        yield 2 ** i
        i += 1
        await asyncio.sleep(0.1)


async def main():
    """Main."""
    # This does *not* introduce concurrent execution
    # It is meant to show syntax only
    _g = [i async for i in mygen()]
    _f = [j async for j in mygen() if not j // 3 % 5]
    _e = [j async for j in mygen() if j // 3 % 5]
    return _g, _f, _e


g, f, e = asyncio.run(main())
print(g)
print(f)
print(e)
