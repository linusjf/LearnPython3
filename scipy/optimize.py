#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from scipy.optimize import least_squares
from scipy.optimize import root
from scipy.optimize import minimize
from scipy.sparse import csr_matrix
from numpy import cos

#Rosenbrock Function
def fun_rosenbrock(x):
   return np.array([10 * (x[1] - x[0]**2), (1 - x[0])])
   
input = np.array([2, 2])
res = least_squares(fun_rosenbrock, input)
print(res)

def func(x):
   return x*2 + 2 * np.cos(x)

sol = root(func, 0.3)
print(sol)

def eqn(x):
  return x**2 + x + 2

mymin = minimize(eqn, 0, method='BFGS')

print(mymin)

def eqn(x):
  return x + cos(x)

myroot = root(eqn, 0)

print(myroot)
print(myroot.x)

arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])

print(csr_matrix(arr))

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

print(csr_matrix(arr).data)

print(csr_matrix(arr).count_nonzero())

mat = csr_matrix(arr)
mat.eliminate_zeros()

print(mat)

mat = csr_matrix(arr)
mat.sum_duplicates()

print(mat)

newarr = csr_matrix(arr).tocsc()

print(newarr)
