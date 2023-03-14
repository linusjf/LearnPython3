#!/usr/bin/env python
"""
Numways.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : numways
# @created     : Tuesday Mar 14, 2023 13:24:21 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
from functools import lru_cache
from math import comb
from timeit import timeit


@lru_cache
def numwayscache(xpos, ypos):
    """Solve recursively using cache."""
    if xpos == 1 or ypos == 1:
        return 1
    return sum([numways(xpos - 1, ypos), numways(xpos, ypos - 1)])


def numways(xpos, ypos):
    """Solve recursively."""
    if xpos == 1 or ypos == 1:
        return 1
    return sum([numways(xpos - 1, ypos), numways(xpos, ypos - 1)])


def numwaysmemo(xpos, ypos, cache=None):
    """Solve with memoization."""
    if cache is None:
        cache = [[-1] * (ypos + 1) for _ in range(xpos + 1)]
    if xpos == 1 or ypos == 1:
        cache[xpos][ypos] = 1
        return 1

    if cache[xpos][ypos] == -1:
        cache[xpos][ypos] = sum(
            [numwaysmemo(xpos - 1, ypos, cache), numwaysmemo(xpos, ypos - 1, cache)]
        )
    return cache[xpos][ypos]


def numwaysdp(xpos, ypos):
    """Solve with dynamic programming."""
    cache = [[0] * ypos for _ in range(xpos)]
    for i in range(xpos):
        cache[i][0] = 1
    for j in range(ypos):
        cache[0][j] = 1
    for i in range(1, xpos):
        for j in range(1, ypos):
            cache[i][j] = cache[i - 1][j] + cache[i][j - 1]
    return cache[xpos - 1][ypos - 1]


def numwaysspace(xpos, ypos):
    """Solve with dynamic programming optimally."""
    cache = [1 for _ in range(ypos)]
    for _ in range(xpos - 1):
        for j in range(1, ypos):
            cache[j] += cache[j - 1]
    return cache[ypos - 1]


def numwayscomb(xpos, ypos):
    """Solve number of ways combinatorial."""
    return comb(xpos + ypos - 2, xpos - 1)


print(numways(5, 4))
print(numwaysmemo(5, 4))
print(numwayscache(5, 4))
print(numwaysdp(5, 4))
print(numwaysspace(5, 4))
print(numwayscomb(5, 4))
print(timeit("numways(5, 4)", number=10000, globals=globals()))
print(timeit("numwaysmemo(5, 4)", number=10000, globals=globals()))
print(timeit("numwayscache(5, 4)", number=10000, globals=globals()))
print(timeit("numwaysdp(5, 4)", number=10000, globals=globals()))
print(timeit("numwaysspace(5, 4)", number=10000, globals=globals()))
print(timeit("numwayscomb(5, 4)", number=10000, globals=globals()))
