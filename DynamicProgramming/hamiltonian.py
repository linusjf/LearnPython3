#!/usr/bin/env python
"""
Hamiltonian.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : hamiltonian
# @created     : Monday Mar 20, 2023 09:06:06 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
from bitset import isbitset


def check_using_dp(adj):
    """Check if graph is Hamiltonian."""
    size = len(adj)
    dparray = [[False] * (2**size) for _ in range(size)]
    for i in range(size):
        dparray[i][2**i] = True
    for i in range(2**size):  # noqa
        for j in range(size):
            if isbitset(j, i):
                for k in range(size):
                    if adj[k][j] and j != k and isbitset(k, i) and dparray[k][i ^ 2**j]:
                        dparray[j][i] = True
                        break
    for i in range(size):
        if dparray[i][2**size - 1]:
            return True
    return False


# Driver Code
ADJ = [[0, 1, 1, 1, 0], [1, 0, 1, 0, 1], [1, 1, 0, 1, 1], [1, 0, 1, 0, 0]]
print(check_using_dp(ADJ))
