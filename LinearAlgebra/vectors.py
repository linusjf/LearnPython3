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
import altair as alt
alt.themes.enable('dark')
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
# multiply two vectors
x, y = np.array([[-2], [2]]), np.array([[4], [-3]])
print(x.T @ y)
# compute L2 norm
x = np.array([[3], [4]])
print(np.linalg.norm(x, 2))
