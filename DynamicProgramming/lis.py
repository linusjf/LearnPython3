#!/usr/bin/env python
"""
Lis.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : lis
# @created     : Thursday Mar 09, 2023 13:42:08 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
from timeit import timeit


def lis(item):
    """Compute longest increasing sequence."""
    size = len(item)
    cache = [1] * size
    for i in range(1, size):
        for j in range(i):
            if item[i] > item[j] and cache[i] < cache[j] + 1:
                cache[i] = cache[j] + 1
    return max(cache)


def lisrecursive(item):
    """Compute lis recursively."""
    size = len(item)
    longest = 1
    for i in range(size):
        longest = max(longest, lisat(item, i))
    return longest


def lisat(item, index):
    """Compute longest subsequence at index."""
    if index == 0:
        return 1
    lishere = 1
    for j in range(index):
        if item[index] > item[j]:
            lishere = max(lishere, lisat(item, j) + 1)
    return lishere


INPUT = [15, 27, 14, 38, 26, 55, 46, 65, 85]
print(lis(INPUT))
print(timeit("lis(INPUT)", number=10000, globals=globals()))
print(lisrecursive(INPUT))
print(timeit("lisrecursive(INPUT)", number=10000, globals=globals()))
INPUT = [3, 4, -1, 0, 6, 2, 3]
print(lis(INPUT))
print(timeit("lis(INPUT)", number=10000, globals=globals()))
print(lisrecursive(INPUT))
print(timeit("lisrecursive(INPUT)", number=10000, globals=globals()))
