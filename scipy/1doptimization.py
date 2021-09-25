#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from scipy import optimize
def f(x):
    return -np.exp(-(x - 0.7)**2)

result = optimize.minimize_scalar(f)
print(result)
# check if solver was successful
print(f"Solver success: {result.success}") 

x_min = result.x
print(f"Min x value: {x_min}") 
print(f"Min value: {result.fun}")
print(f"Iterations: {result.nit}")
print(f"Function evaluations: {result.nfev}")
