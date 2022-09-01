#!/usr/bin/env python
# -*- coding: utf-8 -*-
# sparse matrix
from numpy import array
from scipy.sparse import csr_matrix
# create dense matrix
A = array([
[1, 0, 0, 1, 0, 0],
[0, 0, 2, 0, 0, 1],
[0, 0, 0, 2, 0, 0]])
print(A)
# convert to sparse matrix (CSR method)
S = csr_matrix(A)
print(S)
# reconstruct dense matrix
B = S.todense()
print(B)

# sparsity calculation
from numpy import count_nonzero
# create dense matrix
A = array([
[1, 0, 0, 1, 0, 0],
[0, 0, 2, 0, 0, 1],
[0, 0, 0, 2, 0, 0]])
print(A)
# calculate sparsity
sparsity = 1.0 - count_nonzero(A) / A.size
print(sparsity)
