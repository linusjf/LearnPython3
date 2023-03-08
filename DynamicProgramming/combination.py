#!/usr/bin/env python
"""
Combination.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : combination
# @created     : Wednesday Mar 08, 2023 10:29:44 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
from timeit import timeit


def naivecombination(number, suffix):
    """Naive combination."""
    if suffix == 1:
        return number
    if number == suffix:
        return 1
    return naivecombination(number - 1, suffix) + naivecombination(number - 1, suffix - 1)


def combination(number, suffix, dparr=None):
    """Combine."""
    if suffix == 1:
        return number
    if number == suffix:
        return 1
    if dparr is None:
        dparr = [[None] * suffix for _ in range(number)]

    if dparr[number - 1][suffix - 1] is None:
        dparr[number - 1][suffix - 1] = combination(number - 1, suffix, dparr) + combination(
            number - 1, suffix - 1, dparr
        )
    return dparr[number - 1][suffix - 1]


print(naivecombination(20, 5))
print(timeit("naivecombination(20, 5)", number=10000, globals=globals()))
print(combination(20, 5))
print(timeit("combination(20, 5)", number=10000, globals=globals()))
