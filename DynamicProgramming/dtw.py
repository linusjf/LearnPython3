#!/usr/bin/env python
"""
Dtw.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : dtw
# @created     : Friday Mar 10, 2023 14:13:12 IST
# @description : Dynamic Time Warping
# -*- coding: utf-8 -*-'
######################################################################
"""
import math
from timeit import timeit


def dist(pointx, pointy):
    """Compute distance."""
    return abs(pointx - pointy)


def dtw(sample, test):
    """Compute dynamic time warp."""
    nsize = len(sample)
    msize = len(test)
    table = [[-math.inf] * (msize + 1) for _ in range(nsize + 1)]
    for i in range(1, nsize + 1):
        table[i][0] = math.inf
    for i in range(1, msize + 1):
        table[0][i] = math.inf
    table[0][0] = 0
    for i in range(1, nsize + 1):
        for j in range(1, msize + 1):
            table[i][j] = dist(sample[i - 1], test[j - 1]) + min(
                table[i - 1][j - 1], table[i][j - 1], table[i - 1][j]
            )
    return table[nsize][msize]


SAMPLE = [1, 2, 3, 5, 5, 5, 6]
TEST = [1, 1, 2, 2, 3, 5]
print(dtw(SAMPLE, TEST))
print(timeit("dtw(SAMPLE,TEST)", number=10000, globals=globals()))
