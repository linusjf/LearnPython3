#!/usr/bin/env python
"""
Asyncq.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : asyncq
# @created     : Tuesday Nov 21, 2023 11:16:07 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# asyncq.py
import argparse
import asyncio
import itertools as it
import time
from secrets import randbelow
from secrets import token_hex


async def makeitem(size: int = 5) -> str:
    """Make item."""
    return token_hex(size)


async def randsleep(caller=None) -> None:
    """Random sleep."""
    i = randbelow(11)
    if caller:
        print(f"{caller} sleeping for {i} seconds.")
    await asyncio.sleep(i)


async def produce(name: int, queue: asyncio.Queue) -> None:
    """Produce."""
    num = randbelow(11)
    for _ in it.repeat(None, num):  # Synchronous loop for each single producer
        await randsleep(caller=f"Producer {name}")
        i = await makeitem()
        _elapsed = time.perf_counter()
        await queue.put((i, _elapsed))
        print(f"Producer {name} added <{i}> to queue.")


async def consume(name: int, queue: asyncio.Queue) -> None:
    """Consume."""
    while True:
        await randsleep(caller=f"Consumer {name}")
        i, tms = await queue.get()
        now = time.perf_counter()
        print(f"Consumer {name} got element <{i}>"
              f" in {now-tms:0.5f} seconds.")
        queue.task_done()


async def main(nprod: int, ncon: int):
    """Main."""
    _queue = asyncio.Queue()
    producers = [asyncio.create_task(produce(n, _queue)) for n in range(nprod)]
    consumers = [asyncio.create_task(consume(n, _queue)) for n in range(ncon)]
    await asyncio.gather(*producers)
    # Implicitly awaits consumers, too
    await _queue.join()
    for con in consumers:
        con.cancel()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--nprod", type=int, default=5)
    parser.add_argument("-c", "--ncon", type=int, default=10)
    ns = parser.parse_args()
    start = time.perf_counter()
    asyncio.run(main(**ns.__dict__))
    elapsed = time.perf_counter() - start
    print(f"Program completed in {elapsed:0.5f} seconds.")
