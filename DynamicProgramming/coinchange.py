#!/usr/bin/env python
"""
Coinchange.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : coinchange
# @created     : Friday Mar 10, 2023 10:27:23 IST
# @description : Coin Change Problem
# -*- coding: utf-8 -*-'
######################################################################
"""
import sys
from timeit import timeit


class CoinChange:
    """Solve Coin Change Problem."""

    coins = None
    size = 0

    def __init__(self, coins):
        """Construct object."""
        self.coins = coins
        self.size = len(coins)

    def recursivesolve(self, value):
        """Solve recursively."""
        if value == 0:
            return 0
        if self.coins is None:
            return -1

        res = sys.maxsize
        for i in range(self.size):
            if self.coins[i] <= value:
                result = self.recursivesolve(value - self.coins[i])
                if result != sys.maxsize and result + 1 < res:
                    res = result + 1
        return res

    def dpsolve(self, value):
        """Solve dynamically."""
        if value == 0:
            return 0
        if self.coins is None:
            return -1
        table = [sys.maxsize] * (value + 1)
        table[0] = 0

        for i in range(1, value + 1):
            for j in range(self.size):
                if self.coins[j] <= i:
                    result = table[i - self.coins[j]]
                    if result != sys.maxsize and result + 1 < table[i]:
                        table[i] = result + 1

        if table[value] == sys.maxsize:
            return -1
        return table[value]


COINS = [9, 6, 5, 1]
solver = CoinChange(COINS)
print(solver.recursivesolve(11))
print(timeit("solver.recursivesolve(11)", number=10000, globals=globals()))
print(solver.dpsolve(11))
print(timeit("solver.dpsolve(11)", number=10000, globals=globals()))
