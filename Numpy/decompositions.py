#!/usr/bin/env python
# -*- coding: utf-8 -*-
# LU decomposition
from numpy import array
from scipy.linalg import lu
# define a square matrix
A = array([
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]])
print(A)
# factorize
P, L, U = lu(A)
print("P = {}".format(P))
print("L = {}".format(L))
print("U = {}".format(U))
# reconstruct
B = P.dot(L).dot(U)
print(B)

# QR decomposition
from numpy.linalg import qr
# define rectangular matrix
A = array([
[1, 2],
[3, 4],
[5, 6]])
print(A)
# factorize
Q, R = qr(A, 'complete')
print("Q = {}".format(Q))
print("R = {}".format(R))
# reconstruct
B = Q.dot(R)
print(B)

# Cholesky decomposition
from scipy.linalg import cholesky
# define symmetrical matrix
A = array([
[2, 1, 1],
[1, 2, 1],
[1, 1, 2]])
print(A)
# factorize
L = cholesky(A,lower=True)
print("L = {}".format(L))
# reconstruct
B = L.dot(L.T)
print(B)

# Cholesky decomposition
# define symmetrical matrix
A = array([
[2, 1, 1],
[1, 2, 1],
[1, 1, 2]])
print(A)
# factorize
U = cholesky(A)
print("U = {}".format(U))
# reconstruct
B = U.T.dot(U)
print(B)
