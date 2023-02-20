#!/usr/bin/env python
# -*- coding: utf-8 -*-
# create matrix
from numpy import array

A = array([[1, 2, 3], [4, 5, 6]])
print(A)

# matrix addition
# define first matrix
A = array([[1, 2, 3], [4, 5, 6]])
print(A)
# define second matrix
B = array([[1, 2, 3], [4, 5, 6]])
print(B)
# add matrices
C = A + B
print(C)

# matrix subtraction
# define first matrix
A = array([[1, 2, 3], [4, 5, 6]])
print(A)
# define second matrix
B = array([[0.5, 0.5, 0.5], [0.5, 0.5, 0.5]])
print(B)
# subtract matrices
C = A - B
print(C)

# matrix Hadamard product
# define first matrix
A = array([[1, 2, 3], [4, 5, 6]])
print(A)
# define second matrix
B = array([[1, 2, 3], [4, 5, 6]])
print(B)
# multiply matrices
C = A * B
print(C)

# matrix division
# define first matrix
A = array([[1, 2, 3], [4, 5, 6]])
print(A)
# define second matrix
B = array([[1, 2, 3], [4, 5, 6]])
print(B)
# divide matrices
C = A / B
print(C)

# matrix dot product
# define first matrix
A = array([[1, 2], [3, 4], [5, 6]])
print(A)
# define second matrix
B = array([[1, 2], [3, 4]])
print(B)
# multiply matrices
C = A.dot(B)
print(C)
# multiply matrices with @ operator
D = A @ B
print(D)

# matrix-vector multiplication
# define matrix
A = array([[1, 2], [3, 4], [5, 6]])
print(A)
# define vector
B = array([0.5, 0.5])
print(B)
# multiply
C = A.dot(B)
print(C)

# matrix-scalar multiplication
# define matrix
A = array([[1, 2], [3, 4], [5, 6]])
print(A)
# define scalar
b = 0.5
print(b)
# multiply
C = A * b
print(C)
