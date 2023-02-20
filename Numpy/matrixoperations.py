#!/usr/bin/env python
# -*- coding: utf-8 -*-
# transpose matrix
from numpy import array

# define matrix
A = array([[1, 2], [3, 4], [5, 6]])
print(A)
# calculate transpose
C = A.T
print(C)

# invert matrix
from numpy.linalg import inv

# define matrix
A = array([[1.0, 2.0], [3.0, 4.0]])
print(A)
# invert matrix
B = inv(A)
print(B)
# multiply A and B
I = A.dot(B)
print(I)

# matrix trace
from numpy import trace

# define matrix
A = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(A)
# calculate trace
B = trace(A)
print(B)

# matrix determinant
from numpy.linalg import det
from numpy.linalg import eig
from numpy import prod

# define matrix
A = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(A)
# calculate determinant
B = det(A)
print(B)
# calculate eigen values
B, C = eig(A)
print(B)
print(prod(B))
print("Why isn't the product of eigen values equal to the computed determinant?")

# vector rank
from numpy.linalg import matrix_rank

# rank
v1 = array([1, 2, 3])
print(v1)
vr1 = matrix_rank(v1)
print(vr1)
# zero rank
v2 = array([0, 0, 0, 0, 0])
print(v2)
vr2 = matrix_rank(v2)
print(vr2)

# rank 0
M0 = array([[0, 0], [0, 0]])
print(M0)
mr0 = matrix_rank(M0)
print(mr0)
# rank 1
M1 = array([[1, 2], [2, 4]])
print(M1)
mr1 = matrix_rank(M1)
print(mr1)
# rank 2
M2 = array([[1, 2], [3, 4]])
print(M2)
mr2 = matrix_rank(M2)
print(mr2)
