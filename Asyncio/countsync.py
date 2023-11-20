#!/usr/bin/env python
"""
Countsync.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : countsync
# @created     : Monday Nov 20, 2023 22:13:33 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# countsync.py
import time


def count():
    """Count."""
    print("One")
    time.sleep(1)
    print("Two")


def main():
    """Main."""
    for _ in range(3):
        count()


if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
