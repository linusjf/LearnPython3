#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from scipy.optimize import minimize
 
def objective(w):
    return w[0]**2 + w[1]**2
 
def constraint1(w):
    "Inequality for point (0,0)"
    return -1*w[2] - 1
 
def constraint2(w):
    "Inequality for point (1,2)"
    return w[0] + 2*w[1] + w[2] - 1
 
def constraint3(w):
    "Inequality for point (2,1)"
    return 2*w[0] + w[1] + w[2] - 1
 
# initial guess
w0 = np.array([1, 1, 1])
 
# optimize
bounds = ((-10,10), (-10,10), (-10,10))
constraints = [
    {"type":"ineq", "fun":constraint1},
    {"type":"ineq", "fun":constraint2},
    {"type":"ineq", "fun":constraint3},
]
solution = minimize(objective, w0, method="SLSQP", bounds=bounds, constraints=constraints)
w = solution.x
print("Objective:", objective(w))
print("Solution:", w)
