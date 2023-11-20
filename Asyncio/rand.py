#!/usr/bin/env python
"""
Rand.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : rand
# @created     : Tuesday Nov 21, 2023 04:39:05 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# rand.py
import asyncio
from secrets import randbelow

# ANSI colors
c = (
    "\033[0m",   # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
)


async def makerandom(idx: int, threshold: int = 6) -> int:
    """Make random."""
    print(c[idx + 1] + f"Initiated makerandom({idx}).")
    i = randbelow(10) + 1
    while i <= threshold:
        print(c[idx + 1] + f"makerandom({idx}) == {i} too low; retrying.")
        await asyncio.sleep(idx + 1)
        i = randbelow(10) + 1
    print(c[idx + 1] + f"---> Finished: makerandom({idx}) == {i}" + c[0])
    return i


async def main():
    """Main."""
    res = await asyncio.gather(*(makerandom(i, 10 - i - 1) for i in range(3)))
    return res

if __name__ == "__main__":
    r1, r2, r3 = asyncio.run(main())
    print()
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")
