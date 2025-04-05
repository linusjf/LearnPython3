#!/usr/bin/env python
"""
Rowechelon.

######################################################################
# @author      : linusjf (linusjf@JuliusCaesar)
# @file        : rowechelon
# @created     : Saturday Apr 05, 2025 13:53:26 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import numpy as np

# Function to get the position of pivot in a row
def pivot_idx(r):
    nonZeroIdx = np.nonzero(r)[0]
    print(nonZeroIdx)
    print(len(r))
    val = float('inf') if len(nonZeroIdx) == 0 else nonZeroIdx[0]
    print(val)
    return val

# Function to check if matrix is in ref
def isREF(A):
    pivotIdxs = np.array([pivot_idx(A[i, :]) for i in range(A.shape[0])])
    print(pivotIdxs)
    if (np.ediff1d(pivotIdxs) <= 0).any():
        return False
    return True
    
A = np.array([[1, 0, 2, 0], [0, 4, 6, 4], [0, 0, 7, 8]])
print(A, '\n', ['The matrix is NOT in REF', 'The matrix is  in REF'][isREF(A)])
A = np.array([[0, 0, 2, 0], [0, 4, 6, 4], [0, 0, 7, 8]])
print(A, '\n', ['The matrix is NOT in REF', 'The matrix is  in REF'][isREF(A)])
