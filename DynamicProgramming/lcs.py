#!/usr/bin/env python
"""
Lcs.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : lcs
# @created     : Wednesday Mar 08, 2023 11:36:06 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
from timeit import timeit


def naivelcs(str1, str2, index1, index2):
    """Compute lcs naively."""
    if index1 == 0 or index2 == 0:
        return 0
    if str1[index1 - 1] == str2[index2 - 1]:
        return 1 + naivelcs(str1, str2, index1 - 1, index2 - 1)
    return max(naivelcs(str1, str2, index1, index2 - 1), naivelcs(str1, str2, index1 - 1, index2))


def lcs(str1, str2, dparr=None):
    """Compute longest common subsequence."""
    # find the length of the strings
    index1 = len(str1)
    index2 = len(str2)
    # declaring the array for storing the dp values
    if dparr is None:
        dparr = [[-1] * (index2 + 1) for _ in range(index1 + 1)]
    for i in range(index1 + 1):
        for j in range(index2 + 1):
            if i == 0 or j == 0:
                dparr[i][j] = 0
            elif str1[i - 1] == str2[j - 1]:
                dparr[i][j] = dparr[i - 1][j - 1] + 1
            else:
                dparr[i][j] = max(dparr[i - 1][j], dparr[i][j - 1])
    return dparr[index1][index2]


def lcsopt(str1, str2, dparr=None):
    """Compute longest common subsequence optimally."""
    # find the length of the strings
    index1 = len(str1)
    index2 = len(str2)
    # declaring the array for storing the dp values
    if dparr is None:
        dparr = [[0] * (index2 + 1) for _ in range(2)]
    for i in range(index1 + 1):
        for j in range(index2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dparr[i % 2][j] = dparr[(i - 1) % 2][j - 1] + 1
            else:
                dparr[i % 2][j] = max(dparr[(i - 1) % 2][j], dparr[i % 2][j - 1])
    return dparr[index1 % 2][index2]


def lcsopt2(str1, str2, dparr=None):
    """Compute longest common subsequence optimally again."""
    # find the length of the strings
    index1 = len(str1)
    index2 = len(str2)
    # declaring the array for storing the dp values
    if dparr is None:
        dparr = [0] * (index2 + 1)
    for i in range(1, index1 + 1):
        prev_row = 0
        prev_row_prev_col = 0
        for j in range(1, index2 + 1):
            prev_row_prev_col = prev_row
            prev_row = dparr[j]
            if str1[i - 1] == str2[j - 1]:
                dparr[j] = prev_row_prev_col + 1
            else:
                dparr[j] = max(dparr[j - 1], prev_row)
    return dparr[index2]


def print_lcs(table, string1, string2):
    """Print lcs."""
    stack = []
    i = len(string1)
    j = len(string2)
    while i > 0 and j > 0:
        if table[i - 1][j - 1] == table[i][j] - 1 and string1[i - 1] == string2[j - 1]:
            stack.append(string1[i - 1])
            i = i - 1
            j = j - 1
        elif table[i - 1][j] == table[i][j]:
            i = i - 1
        else:
            j = j - 1
    while len(stack) != 0:
        print(stack.pop(), end=" ")
    print()


X = "AGGTAB"
Y = "GXTXAYB"
print(X, Y)
print(lcsopt2(X, Y))
print(timeit("lcsopt2(X,Y)", number=10000, globals=globals()))
print(lcsopt(X, Y))
print(timeit("lcsopt(X,Y)", number=10000, globals=globals()))
cache = [[-1] * (len(Y) + 1) for _ in range(len(X) + 1)]
print(lcs(X, Y, cache))
print_lcs(cache, X, Y)
print(timeit("lcs(X,Y, cache)", number=10000, globals=globals()))
print(naivelcs(X, Y, len(X), len(Y)))
print(timeit("naivelcs(X,Y, len(X), len(Y))", number=10000, globals=globals()))
