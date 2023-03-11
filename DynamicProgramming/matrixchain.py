#!/usr/bin/env python
"""
Matrixchain.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : matrixchain
# @created     : Saturday Mar 11, 2023 12:01:24 IST
# @description : Matrix Chain Optimization
# -*- coding: utf-8 -*-
######################################################################
"""
import sys
from timeit import timeit
import functools


class MatrixChain:
    """Solve matrix chain optimization."""

    matrices = None

    def __init__(self, matrices):
        """Construct Matrix Chain."""
        self.matrices = matrices

    def recursolve(self, i, j):
        """Solve recursively."""
        if self.matrices is None:
            return -1
        if i == j:
            return 0
        minimum = sys.maxsize
        for k in range(i, j):
            count = (
                self.recursolve(i, k)
                + self.recursolve(k + 1, j)  # noqa
                + self.matrices[i - 1] * self.matrices[k] * self.matrices[j]  # noqa
            )
            minimum = min(count, minimum)

        return minimum

    @functools.lru_cache(maxsize=128)
    def cachedsolve(self, i, j):
        """Solve recursively."""
        if self.matrices is None:
            return -1
        if i == j:
            return 0
        minimum = sys.maxsize
        for k in range(i, j):
            count = (
                self.recursolve(i, k)
                + self.recursolve(k + 1, j)  # noqa
                + self.matrices[i - 1] * self.matrices[k] * self.matrices[j]  # noqa
            )
            if count < minimum:
                minimum = count

        return minimum

    def dpsolve(self, i, j, cache=None):
        """Solve dynamically."""
        if self.matrices is None:
            return -1
        if i == j:
            return 0
        length = len(self.matrices) + 1
        if cache is None:
            cache = [[-1] * (length + 1) for _ in range(length + 1)]
        if cache[i][j] != -1:
            return cache[i][j]
        minimum = sys.maxsize
        for k in range(i, j):
            count = (
                self.dpsolve(i, k, cache)
                + self.dpsolve(k + 1, j, cache)  # noqa
                + self.matrices[i - 1] * self.matrices[k] * self.matrices[j]  # noqa
            )
            minimum = min(count, minimum)

        cache[i][j] = minimum
        return cache[i][j]


ARR = [1, 2, 3, 4, 3, 7, 9, 11]
chain = MatrixChain(ARR)
print(chain.recursolve(1, len(ARR) - 1))
print(timeit("chain.recursolve(1, len(ARR) - 1)", number=1, globals=globals()))
print(chain.cachedsolve(1, len(ARR) - 1))
print(timeit("chain.cachedsolve(1, len(ARR) - 1)", number=1, globals=globals()))
print(chain.dpsolve(1, len(ARR) - 1))
print(timeit("chain.dpsolve(1, len(ARR) - 1)", number=1, globals=globals()))
