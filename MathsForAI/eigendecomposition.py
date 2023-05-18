#!/usr/bin/env python
"""
Eigendecomposition.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : eigendecomposition
# @created     : Thursday May 18, 2023 08:42:28 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import sys
import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg
from matplotlib.backends.backend_pdf import PdfPages

print(f"Python version {sys.version}")
print(f"Numpy version: {np.__version__}")
pp = PdfPages("eigendecomposition.pdf")
print("Setup Complete")


# define an array
A = np.arange(9) - 3
print(A)
B = A.reshape((3, 3))
print(B)
# Euclidean L2 norm -- default
print(linalg.norm(A))
print(linalg.norm(B))
# Frogenius norm is the L2 norm for a matrix
print(linalg.norm(B, "fro"))
# max norm P = infinity
print(linalg.norm(A, np.inf))
print(linalg.norm(B, np.inf))
# L1 norm
print(linalg.norm(A, 1))
print(linalg.norm(B, 1))
# vector normalization - normalization to produce a unit vector
norm = linalg.norm(A)
A_unit = A / norm
print(A_unit)
# the magnitude of unit vector is 1
print(linalg.norm(A_unit))

# find the eigen values and eigen vectors for a simple square matrix
C = np.diag(np.arange(1, 4))
print(C)
eigenvalues, eigenvectors = linalg.eig(C)
print(eigenvalues, eigenvectors)
# the eigen value w[i] corresponds to the eigen vector v[:, i]
for i in range(3):
    print(f"Eigen value: {eigenvalues[i]}")
    print(f"Eigen vector: {eigenvectors[:, i]}")
# verify eigen decomposition
diag = np.diag(eigenvalues)
print(diag)
vinverse = linalg.inv(eigenvectors)
mul = np.matmul(diag, vinverse)
val = np.matmul(eigenvectors, mul)
print(val)

# plot the eigen vectors
origin = [0, 0, 0]
fig = plt.figure(figsize=(18, 10))
ax1 = fig.add_subplot(121, projection="3d")
ax1.quiver(
    origin, origin, origin, eigenvectors[0, :], eigenvectors[1, :],
    eigenvectors[2, :], color="k"
)
ax1.set_xlim([-3, 3])
ax1.set_ylim([-3, 3])
ax1.set_zlim([-3, 3])
ax1.set_xlabel("X-axis")
ax1.set_ylabel("Y-axis")
ax1.set_zlabel("Z-axis")
ax1.view_init(15, 30)
ax1.set_title("Before multiplication")

new_eig = np.matmul(C, eigenvectors)
ax2 = fig.add_subplot(122, projection="3d")
ax2.quiver(origin, origin, origin, new_eig[0, :], new_eig[1, :], new_eig[2, :],
           color="k")
# add the eigen values to the plot
ax2.plot(
    eigenvalues[0] * eigenvectors[0],
    eigenvalues[1] * eigenvectors[1],
    eigenvalues[2] * eigenvectors[2],
    "rX",
)
ax2.set_xlim([-3, 3])
ax2.set_ylim([-3, 3])
ax2.set_zlim([-3, 3])
ax2.set_xlabel("X-axis")
ax2.set_ylabel("Y-axis")
ax2.set_zlabel("Z-axis")
ax2.view_init(15, 30)
ax2.set_title("After multiplication")

# show plot
plt.plot(origin, origin)
pp.savefig()
pp.close()
