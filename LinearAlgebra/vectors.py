#!/usr/bin/env python
"""
Vectors.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : vectors
# @created     : Wednesday Oct 18, 2023 09:03:59 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import numpy as np
import pandas as pd
import seaborn as sns
x = np.array([[1],
              [2],
              [3]])
# (3 dimensions, 1 element on each)
print(x.shape)
print(f'A 3-dimensional vector:\n{x}')
x = y = np.array([[1],
                  [2],
                  [3]])
print(x + y)
print(np.add(x, y))
ALPHA = 2
x = np.array([[1],
              [2],
              [3]])
print(ALPHA * x)
a, b = 2, 3
x, y = np.array([[2], [3]]), np.array([[4], [5]])
print(a*x + b*y)
# compute vector multiplication
x, y = np.array([[-2], [2]]), np.array([[4], [-3]])
print(x.T @ y)
# compute L2 norm
x = np.array([[3], [4]])
print(np.linalg.norm(x, 2))
# compute Manhattan norm
x = np.array([[3], [-4]])
print(np.linalg.norm(x, 1))
# compute max norm
x = np.array([[3], [-4]])
print(np.linalg.norm(x, np.inf))
x, y = np.array([[-2], [2]]), np.array([[4], [-3]])
print(x.T @ y)
# To compute the L2 distance between a pair of vectors:
distance = np.linalg.norm(x-y, 2)
print(f'L_2 distance : {distance}')
x, y = np.array([[1], [2]]), np.array([[5], [7]])
# here we translate the cos(theta) definition
cos_theta = (x.T @ y) / (np.linalg.norm(x, 2) * np.linalg.norm(y, 2))
print(f'cos of the angle = {np.round(cos_theta, 3)}')
# to know the exact value of θ
# we need to take the trigonometric inverse of the cosine function as:
cos_inverse = np.arccos(cos_theta)
print(f'angle in radians = {np.round(cos_inverse, 3)}')
# from radiants to degrees we can use the following formula:
degrees = cos_inverse * ((180)/np.pi)
print(f'angle in degrees = {np.round(degrees, 3)}')
# Here is an example of orthogonal vectors
x = np.array([[2], [0]])
y = np.array([[0], [2]])
cos_theta = (x.T @ y) / (np.linalg.norm(x, 2) * np.linalg.norm(y, 2))
print(f'cos of the angle = {np.round(cos_theta, 3)}')
# We see that this vectors are orthogonal as cosθ=0
# . This is equal to ≈1.57
cos_inverse = np.arccos(cos_theta)
degrees = cos_inverse * ((180)/np.pi)
print(f'angle in radians = {np.round(cos_inverse, 3)}')
print(f'angle in degrees ={np.round(degrees, 3)} ')
df = pd.DataFrame({"x1": [0, 2], "y1": [8, 3], "x2": [0.5, 2], "y2": [0, 3]})
lp = sns.lineplot(data=df, x="x1", y="y1")
lp = sns.lineplot(data=df, x="x2", y="y2")
lp.set(xlabel="x1, x2", ylabel="y1, y2", title="Vectors")
fig = lp.get_figure()
fig.savefig("vectors.pdf")
