#!/usr/bin/env python
"""
Countasync.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : countasync
# @created     : Monday Nov 20, 2023 21:41:53 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# countasync.py
import asyncio


async def count():
    """Count."""
    print("One")
    await asyncio.sleep(1)
    print("Two")


async def main():
    """Main."""
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
