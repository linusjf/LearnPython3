#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import linspace

def f(x):
    return x

def g(x):
    return x**2

N = int(input('Give the number of check points N: '))
epsilon = float(input('Give the error tolerance: '))

x_values = linspace(-4, 4, N)

# Next, we run over all indices in the array `x_values` and
# check if the difference between function values is smaller than
# the chosen limit

for i in range(N):
    if abs(f(x_values[i]) - g(x_values[i])) < epsilon:
        print(x_values[i])
