#!/usr/bin/env python
"""
Reducedrowechelon.

######################################################################
# @author      : linusjf (linusjf@JuliusCaesar)
# @file        : reducedrowechelon
# @created     : Saturday Apr 05, 2025 19:50:25 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import numpy as np

# Function to get the position of pivot in a row
def pivot_idx(r):
    nonZeroIdx = np.nonzero(r)[0]
    return float('inf') if len(nonZeroIdx) == 0 else nonZeroIdx[0]

# Function to check if matrix is in ref
def isREF(A):
    pivotIdxs = np.array([pivot_idx(A[i, :]) for i in range(A.shape[0])])
    if (np.ediff1d(pivotIdxs) <= 0).any():
        return False
    return True

# Function to check if matrix is in rref
def isRREF(A):
    if not(isREF(A)):
        return False
    else:
      print("Row Echelon Form")
    for i in range(A.shape[0]):
        pIdx = pivot_idx(A[i, :])
        if pIdx < A.shape[1]:
            # check the pivot and the other values of the column
            Z = np.zeros((A.shape[0]))
            Z[i] = 1
            Cp = A[:, pIdx]
            if np.sum((Cp - Z)**2) > 0.00000001:
                return False
    return True
    
A = np.array([[1, 8, 0, 1, 4, 0], 
              [0, 0, 1, 3, 5, 0], 
              [0, 0, 0, 0, 0, 1]])
print(A, '\n', ['The matrix is NOT in RREF', 'The matrix is  in RREF'][isRREF(A)])
