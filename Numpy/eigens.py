#!/usr/bin/env python
# -*- coding: utf-8 -*-
# eigendecomposition
from numpy import array
from numpy.linalg import det
from numpy import prod
from numpy.linalg import eig
# define matrix
A = array([
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]])
print(A)
# factorize
values, vectors = eig(A)
print(values)
print(vectors)
print(det(A))
print(prod(values))

# confirm eigenvector
from numpy import array
from numpy.linalg import eig
# define matrix
A = array([
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]])
# factorize
values, vectors = eig(A)
print(values)
print(vectors)
# confirm first eigenvector
B = A.dot(vectors[:, 0])
print(B)
C = vectors[:, 0] * values[0]
print(C)
# confirm second eigenvector
B = A.dot(vectors[:, 1])
print(B)
C = vectors[:, 1] * values[1]
print(C)
# confirm third eigenvector
B = A.dot(vectors[:, 2])
print(B)
C = vectors[:, 2] * values[2]
print(C)

# reconstruct matrix
from numpy import diag
from numpy.linalg import inv
# define matrix
A = array([
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]])
print(A)
# factorize
values, vectors = eig(A)
# create matrix from eigenvectors
Q = vectors
# create inverse of eigenvectors matrix
R = inv(Q)
# create diagonal matrix from eigenvalues
L = diag(values)
# reconstruct the original matrix
B = Q.dot(L).dot(R)
print(B)
