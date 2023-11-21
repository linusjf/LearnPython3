#!/usr/bin/env python
"""
Chained.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : chained
# @created     : Tuesday Nov 21, 2023 08:36:23 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# chained.py
import asyncio
from secrets import randbelow
import time
import sys


async def part1(num: int) -> int:
    """Compute part1."""
    i = randbelow(num)
    print(f"part1({num}) sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = i
    print(f"Returning part1({num}) == {result}.")
    return result


async def part2(num: int, arg: int) -> int:
    """Compute part2."""
    i = randbelow(num)
    print(f"part2{num, arg} sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = operation(arg, i)
    print(f"Returning part2{num, arg} == {result}.")
    return result


def operation(num: int, num2: int) -> int:
    """Perform operation."""
    oper = randbelow(4)
    match oper:
        case 0:
            return num + num2
        case 1:
            return num - num2
        case 2:
            return num // num2
        case 3:
            return num * num2


async def chain(num: int) -> None:
    """Chain."""
    _start = time.perf_counter()
    _p1 = await part1(num)
    _p2 = await part2(num, _p1)
    _end = time.perf_counter() - _start
    print(f"-->Chained result{num} => {_p2} (took {_end:0.2f} seconds).")


async def main(*_args):
    """Main."""
    await asyncio.gather(*(chain(n) for n in _args))

if __name__ == "__main__":
    args = [1, 2, 3] if len(sys.argv) == 1 else map(int, sys.argv[1:])
    start = time.perf_counter()
    asyncio.run(main(*args))
    end = time.perf_counter() - start
    print(f"Program finished in {end:0.2f} seconds.")
