#!/usr/bin/env python
"""
Profit.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : profit
# @created     : Wednesday Mar 08, 2023 14:32:58 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
from timeit import timeit

profits = [2, 3, 5, 1, 4]
COUNT = len(profits)


def naiveprofit(begin, end):
    """Compute profit naively."""
    if begin > end:
        return 0
    year = COUNT - end + begin
    return max(
        naiveprofit(begin + 1, end) + year * profits[begin],
        naiveprofit(begin, end - 1) + year * profits[end],
    )


def profit(begin, end, cache=None):
    """Compute profit dynamically."""
    if begin > end:
        return 0
    if cache is None:
        cache = [[None] * COUNT for _ in range(COUNT)]
    year = COUNT - end + begin
    if cache[begin][end] is None:
        cache[begin][end] = max(
            profit(begin + 1, end, cache) + year * profits[begin],
            profit(begin, end - 1, cache) + year * profits[end],
        )
    return cache[begin][end]


print(naiveprofit(0, COUNT - 1))
print(timeit("naiveprofit(0, COUNT - 1)", number=10000, globals=globals()))
print(profit(0, COUNT - 1))
print(timeit("profit(0, COUNT - 1)", number=10000, globals=globals()))
