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


def lcs(str1, str2):
    """Compute longest common subsequence."""
    # find the length of the strings
    index1 = len(str1)
    index2 = len(str2)
    # declaring the array for storing the dp values
    dparr = [[None] * (index2 + 1) for _ in range(index1 + 1)]
    for i in range(index1 + 1):
        for j in range(index2 + 1):
            if i == 0 or j == 0:
                dparr[i][j] = 0
            elif str1[i - 1] == str2[j - 1]:
                dparr[i][j] = dparr[i - 1][j - 1] + 1
            else:
                dparr[i][j] = max(dparr[i - 1][j], dparr[i][j - 1])

    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return dparr[index1][index2]


X = "AGGTAB"
Y = "GXTXAYB"
print(lcs(X, Y))
print(timeit("lcs(X,Y)", number=10000, globals=globals()))
print(naivelcs(X, Y, len(X), len(Y)))
print(timeit("naivelcs(X,Y, len(X), len(Y))", number=10000, globals=globals()))
