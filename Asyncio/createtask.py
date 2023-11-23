#!/usr/bin/env python
"""
Createtask.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : createtask
# @created     : Thursday Nov 23, 2023 05:17:02 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import asyncio
import time


async def coro(seq) -> list:
    """'IO' wait time is proportional to the max element."""
    await asyncio.sleep(max(seq))
    return list(reversed(seq))


async def main():
    """Main."""
    # This is a bit redundant in the case of one task
    # We could use `await coro([3, 2, 1])` on its own
    # Python 3.7+
    task = asyncio.create_task(coro([3, 2, 1]))
    ret = await task
    print(f'task: type {type(task)}')
    print(f'task done: {task.done()}')
    return ret

t = asyncio.run(main())
print(t)


async def main2():
    """Main 2."""
    task = asyncio.create_task(coro([3, 2, 1]))
    task2 = asyncio.create_task(coro([10, 5, 0]))  # Python 3.7+
    print('Start:', time.strftime('%X'))
    _a = await asyncio.gather(task, task2)
    print('End:', time.strftime('%X'))  # Should be 10 seconds
    print(f'Both tasks done: {all((task.done(), task2.done()))}')
    return _a

a = asyncio.run(main2())
print(a)


async def main3():
    """Main 3."""
    task = asyncio.create_task(coro([3, 2, 1]))
    task2 = asyncio.create_task(coro([10, 5, 0]))
    print('Start:', time.strftime('%X'))
    for res in asyncio.as_completed((task, task2)):
        compl = await res
        print(f'res: {compl} completed at {time.strftime("%X")}')
    print('End:', time.strftime('%X'))
    print(f'Both tasks done: {all((task.done(), task2.done()))}')

asyncio.run(main3())
