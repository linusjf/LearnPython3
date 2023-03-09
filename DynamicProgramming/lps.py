#!/usr/bin/env python
"""
Lps.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : lps
# @created     : Thursday Mar 09, 2023 20:59:25 IST
# @description : Longest Palindromic Subsequence
# -*- coding: utf-8 -*-'
######################################################################
"""
from timeit import timeit


def lps(item):
    """Compute length of longest palindromic subsequence."""
    size = len(item)
    cache = [[0] * size for _ in range(size)]
    for i in range(size):
        cache[i][i] = 1
    for i in range(size - 2):
        if item[i] == item[i + 1]:
            cache[i][i + 1] = 2
        else:
            cache[i][i + 1] = 1
    length = 3
    while length <= size:
        for i in range(size - length):
            j = i + length - 1
            if item[i] == item[j]:
                cache[i][j] = 2 + cache[i + 1][j - 1]
            else:
                cache[i][j] = max(cache[i + 1][j], cache[i][j - 1])
        length = length + 1
    return cache[0][size - 2]


INPUT = "agbdba"
print(lps(INPUT))
print(timeit("lps(INPUT)", number=10000, globals=globals()))
INPUT = "GEEKSFORGEEKS"
print(lps(INPUT))
print(timeit("lps(INPUT)", number=10000, globals=globals()))
