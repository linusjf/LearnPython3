#!/usr/bin/env python
"""
Mincost.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : mincost
# @created     : Tuesday Mar 14, 2023 08:36:51 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
from functools import lru_cache
import sys
from timeit import timeit


def min_cost_dp(cost, dest_row, dest_col):
    """Solve min cost."""
    cols = len(cost[0])
    rows = len(cost)
    tcarray = [[0 for _ in range(cols)] for _ in range(rows)]
    tcarray[0][0] = cost[0][0]
    # Initialize first column of total cost(tc) array
    for i in range(1, dest_row + 1):
        tcarray[i][0] = tcarray[i - 1][0] + cost[i][0]
    # Initialize first row of tc array
    for j in range(1, dest_col + 1):
        tcarray[0][j] = tcarray[0][j - 1] + cost[0][j]

    # Construct rest of the tc array
    for i in range(1, dest_row + 1):
        for j in range(1, dest_col + 1):
            tcarray[i][j] = (
                min(tcarray[i - 1][j - 1], tcarray[i - 1][j], tcarray[i][j - 1]) + cost[i][j]
            )
    return tcarray[dest_row][dest_col]


@lru_cache
def min_cost_cache(cost, dest_row, dest_col):
    """Solve recursively."""
    if dest_col < 0 or dest_row < 0:
        return sys.maxsize
    if dest_row == 0 and dest_col == 0:
        return cost[dest_row][dest_col]
    return (
        min(
            min_cost_cache(cost, dest_row - 1, dest_col - 1),
            min_cost_cache(cost, dest_row, dest_col - 1),
            min_cost_cache(cost, dest_row - 1, dest_col),
        )
        + cost[dest_row][dest_col]
    )


def min_cost(cost, dest_row, dest_col):
    """Solve recursively."""
    if dest_col < 0 or dest_row < 0:
        return sys.maxsize
    if dest_row == 0 and dest_col == 0:
        return cost[dest_row][dest_col]
    return (
        min(
            min_cost(cost, dest_row - 1, dest_col - 1),
            min_cost(cost, dest_row, dest_col - 1),
            min_cost(cost, dest_row - 1, dest_col),
        )
        + cost[dest_row][dest_col]
    )


# Driver program to test above functions
COST = tuple([tuple([1, 2, 3, 4]), tuple([4, 8, 2, 6]), tuple([1, 5, 3, 9])])

print(min_cost(COST, 2, 3))
print(timeit("min_cost(COST, 2, 3)", number=1, globals=globals()))
time_recur = timeit("min_cost(COST, 2, 3)", number=1, globals=globals())
print(min_cost_dp(COST, 2, 3))
print(timeit("min_cost_dp(COST, 2, 3)", number=1, globals=globals()))
time_dp = timeit("min_cost_dp(COST, 2, 3)", number=1, globals=globals())
print(min_cost_cache(COST, 2, 3))
print(timeit("min_cost_cache(COST, 2, 3)", number=1, globals=globals()))
time_cache = timeit("min_cost_cache(COST, 2, 3)", number=1, globals=globals())
print(f"Using lru_cache is {time_recur/time_cache} times faster than recursive solution.")
print(f"Using dynamic programming is {time_recur/time_dp} times faster than recursive solution.")
print(f"Using lru_cache is {time_dp/time_cache} times faster than dynamic programming solution.")
