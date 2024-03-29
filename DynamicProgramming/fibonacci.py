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
import math
from timeit import timeit


def naivefib(_n):
    """Naive Fibonacci."""
    if _n <= 2:
        return 1
    return naivefib(_n - 1) + naivefib(_n - 2)


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


def spacefib(_n):  # noqa
    """Space Fibonacci."""
    _a = 0
    _b = 1
    if _n == 0:
        return _a
    if _n in (1, 2):
        return _b
    for _i in range(2, _n + 1):
        _c = _a + _b
        _a = _b
        _b = _c
    return _b


def powerfib(num):  # noqa
    """Power Fib."""
    fibmat = [[1, 1], [1, 0]]
    if num == 0:
        return 0
    if num in (1, 2):
        return 1
    power(fibmat, num - 1)
    return fibmat[0][0]


def multiply(fibmat, mat):
    """Multiply."""
    xval = fibmat[0][0] * mat[0][0] + fibmat[0][1] * mat[1][0]

    yval = fibmat[0][0] * mat[0][1] + fibmat[0][1] * mat[1][1]

    zval = fibmat[1][0] * mat[0][0] + fibmat[1][1] * mat[1][0]

    wval = fibmat[1][0] * mat[0][1] + fibmat[1][1] * mat[1][1]

    fibmat[0][0] = xval
    fibmat[0][1] = yval
    fibmat[1][0] = zval
    fibmat[1][1] = wval


def power(fibmat, num):
    """Power optimized."""
    if num in (0, 1):
        return
    mat = [[1, 1], [1, 0]]
    power(fibmat, num // 2)
    multiply(fibmat, fibmat)
    if num % 2 != 0:
        multiply(fibmat, mat)


def recurfib(num, fibarr=None):
    """Recur Fibonacci."""
    # Base cases
    if num == 0:
        return 0
    if num in (1, 2):
        return 1
    if fibarr is None:
        fibarr = [None] * num
    # If fib(n) is already computed
    if fibarr[num - 1]:
        return fibarr[num - 1]
    if num & 1:
        k = (num + 1) // 2
        fibarr[num - 1] = fib(k) * fib(k) + fib(k - 1) * fib(k - 1)
    else:
        k = num // 2
        fibarr[num - 1] = (2 * fib(k - 1) + fib(k)) * fib(k)
    return fibarr[num - 1]


def binetfib(num):
    """Binet Fibonacci."""
    phi = (1 + math.sqrt(5)) / 2
    return round(pow(phi, num) / math.sqrt(5))


print(naivefib(15))
print(timeit("naivefib(15)", number=10000, globals=globals()))
print(fib(15))
print(timeit("fib(15)", number=10000, globals=globals()))
print(spacefib(15))
print(timeit("spacefib(15)", number=10000, globals=globals()))
print(powerfib(15))
print(timeit("powerfib(15)", number=10000, globals=globals()))
print(recurfib(15))
print(timeit("recurfib(15)", number=10000, globals=globals()))
print(binetfib(15))
print(timeit("binetfib(15)", number=10000, globals=globals()))
