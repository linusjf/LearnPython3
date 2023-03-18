#!/usr/bin/env python
"""
Assignment.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : assignment
# @created     : Saturday Mar 18, 2023 11:07:01 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
from math import inf as infinity
import bitset


def assign_tasks(costs):
    """Assign tasks while minimizing total cost."""
    size = len(costs)
    dparray = [infinity] * (2**size)
    dparray[0] = 0
    for mask in range(2**size):
        count = bitset.count_set_bits(mask, size)
        for j in range(size):
            if not bitset.isbitset(j, mask):
                dparray[mask | (1 << j)] = min(
                    dparray[mask | (1 << j)], dparray[mask] + costs[count][j]
                )
    return dparray[2**size - 1]


COSTS = [[5, 2, 3, 4, 5], [4, 3, 2, 6, 8], [12, 15, 10, 6, 8], [2, 4, 6, 7, 8], [4, 6, 8, 9, 6]]
print(assign_tasks(COSTS))
COSTS = [[5, 2, 3], [4, 3, 2], [12, 15, 10]]
print(assign_tasks(COSTS))
