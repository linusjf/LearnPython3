#!/usr/bin/env python3
"""Scipy examples."""
import numpy as np
from scipy import linalg

# pylint: disable=no-name-in-module
from scipy.special import comb, exp10, perm

# find combinations of 5, 2 values using comb(N, k)
COM = comb(5, 2, exact=False, repetition=True)
print(COM)

# find permutation of 5, 2 using perm (N, k) function
PER = perm(5, 2, exact=True)
print(PER)

EXP = exp10([1, 10])
print(EXP)

# define square matrix
TWO_D_ARRAY = np.array([[4, 5], [3, 2]])
# pass values to det() function
print(linalg.det(TWO_D_ARRAY))
print(linalg.inv(TWO_D_ARRAY))

ARR = np.array([[5, 4], [6, 3]])
# pass value into function
EG_VAL, EG_VECT = linalg.eig(ARR)
# get eigenvalues
print(EG_VAL)
# get eigenvectors
print(EG_VECT)
# pylint: enable=no-name-in-module
