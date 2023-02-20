#!/usr/bin/env python
# -*- coding: utf-8 -*-
# triangular matrices
from numpy import array
from numpy import tril
from numpy import triu

# define square matrix
M = array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print(M)
# lower triangular matrix
lower = tril(M)
print(lower)
# upper triangular matrix
upper = triu(M)
print(upper)

# diagonal matrix
from numpy import diag

# define square matrix
M = array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print(M)
# extract diagonal vector
d = diag(M)
print(d)
# create diagonal matrix from vector
D = diag(d)
print(D)

# identity matrix
from numpy import identity

I = identity(3)
print(I)

# orthogonal matrix
from numpy.linalg import inv

# define orthogonal matrix
Q = array([[1, 0], [0, -1]])
print(Q)
# inverse equivalence
V = inv(Q)
print(Q.T)
print(V)
# identity equivalence
I = Q.dot(Q.T)
print(I)
# identity equivalence
I = Q.dot(V)
print(I)
