#!/usr/bin/env python
"""
Boymeetsgirl.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : boymeetsgirl
# @created     : Friday Mar 17, 2023 11:43:55 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# from timeit import timeit


def solve_for_cals(workout):  # noqa MC0001
    """Solve for calories."""
    rows = len(workout)
    cols = len(workout[0])
    boyarr1 = [[-1] * cols for _ in range(rows)]
    boyarr2 = [[-1] * cols for _ in range(rows)]
    girlarr1 = [[-1] * cols for _ in range(rows)]
    girlarr2 = [[-1] * cols for _ in range(rows)]

    for i in range(1, rows):
        for j in range(1, cols):
            boyarr1[i][j] = max(boyarr1[i - 1][j], boyarr1[i][j - 1]) + workout[i][j]
    for i in reversed(range(rows - 1)):
        for j in reversed(range(cols - 1)):
            boyarr2[i][j] = max(boyarr2[i + 1][j], boyarr2[i][j + 1]) + workout[i][j]
    for i in range(1, rows):
        for j in range(1, cols):
            girlarr1[i][j] = max(girlarr1[i - 1][j], girlarr1[i][j - 1]) + workout[i][j]
    for i in reversed(range(rows - 1)):
        for j in reversed(range(cols - 1)):
            girlarr2[i][j] = max(girlarr2[i + 1][j], girlarr2[i][j + 1]) + workout[i][j]

    ans = 0
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            op1 = boyarr1[i][j - 1] + boyarr2[i][j + 1] + girlarr1[i + 1][j] + girlarr2[i - 1][j]
            op2 = boyarr1[i - 1][j] + boyarr2[i + 1][j] + girlarr1[i][j - 1] + girlarr2[i][j + 1]
            ans = max(ans, max(op1, op2))

    return ans


# driver code
WORKOUT = [[26, 30, 46, 35], [45, 28, 36, 48], [32, 65, 26, 57]]
print(solve_for_cals(WORKOUT))
