#!/usr/bin/env python
"""
Helloworld.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : helloworld
# @created     : Wednesday Nov 22, 2023 06:00:15 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import asyncio


async def main():
    """Main."""
    print("Hello ...")
    await asyncio.sleep(1)
    print("World!")

ROUTINE = main()
asyncio.run(ROUTINE)
