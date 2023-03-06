#!/usr/bin/env python
"""
Fibonacci.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : fibonacci
# @created     : Monday Mar 06, 2023 21:19:48 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
from timeit import timeit


def fib(_n, _dp=None):
    """Fibonacci."""
    if _n in (1, 2):
        return 1
    if _dp is None:
        _dp = [None] * _n
    if _dp[_n - 1] is not None:
        return _dp[_n - 1]
    _dp[_n - 1] = fib(_n - 1, _dp) + fib(_n - 2, _dp)
    return _dp[_n - 1]


print(timeit("fib(100)", number=100000, globals=globals()))
