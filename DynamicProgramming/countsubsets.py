#!/usr/bin/env python
"""
Countsubsets.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : countsubsets
# @created     : Friday Mar 17, 2023 21:29:54 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import bitset


def count_subsets(dataset, val):
    """Count subsets."""
    set_size = len(dataset)
    count = 0
    for element in range(2**set_size):
        total = 0
        for k in range(set_size):
            if bitset.isbitset(k, element):
                total = total + dataset[k]
        if total >= val:
            count = count + 1
    return count


A = [1, 2, 3]
print(count_subsets(A, 4))
A = [1, 2, 3, 4]
print(count_subsets(A, 4))
