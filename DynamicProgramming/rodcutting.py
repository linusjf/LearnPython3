#!/usr/bin/env python
"""
Rodcutting.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : rodcutting
# @created     : Saturday Mar 11, 2023 16:40:04 IST
# @description : Returns the best obtainable price for a rod of length n
                and price[] as prices of different pieces
# -*- coding: utf-8 -*-'
######################################################################
"""
import sys
from timeit import timeit
from functools import lru_cache


def cutrod(price, num):
    """Solve cutrod recursively."""
    if num <= 0:
        return 0
    max_val = -sys.maxsize - 1
    # Recursively cut the rod in different pieces
    # and compare different configurations
    for i in range(0, num):
        max_val = max(max_val, price[i] + cutrod(price, num - i - 1))
    return max_val


@lru_cache(maxsize=None)
def cachecutrod(price, num):
    """Solve cutrod recursively using lru cache."""
    if num <= 0:
        return 0
    max_val = -sys.maxsize - 1
    for i in range(0, num):
        max_val = max(max_val, price[i] + cutrod(price, num - i - 1))
    return max_val


def dpcutrod(price, num):
    """Solve cutrod dynamically."""
    val = [0] * (num + 1)
    if num <= 0:
        return 0
    for i in range(1, num + 1):
        max_val = -sys.maxsize - 1
        for j in range(i):
            max_val = max(max_val, price[j] + val[i - j - 1])
            val[i] = max_val

    return val[num]


# Driver code
arr = [1, 5, 8, 9, 10, 17, 17, 20]
SIZE = len(arr)

print(cutrod(arr, SIZE))
print(timeit("cutrod(arr, SIZE)", number=10000, globals=globals()))
print(cachecutrod(tuple(arr), SIZE))
print(timeit("cachecutrod(tuple(arr), SIZE)", number=10000, globals=globals()))
print(dpcutrod(arr, SIZE))
print(timeit("dpcutrod(arr, SIZE)", number=10000, globals=globals()))
