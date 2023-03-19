#!/usr/bin/env python
"""
Scipyhungarian.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : scipyhungarian
# @created     : Saturday Mar 18, 2023 21:09:21 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import numpy as np
from scipy.optimize import linear_sum_assignment  # type: ignore

cost = np.array([[4, 1, 3], [2, 0, 5], [3, 2, 2]])
row_ind, col_ind = linear_sum_assignment(cost)
print(row_ind, col_ind)
print(cost[row_ind, col_ind].sum())
cost = np.array(
    [[7, 6, 2, 9, 2], [6, 2, 1, 3, 9], [5, 6, 8, 9, 5], [6, 8, 5, 8, 6], [9, 5, 6, 4, 7]]
)
row_ind, col_ind = linear_sum_assignment(cost)
print(row_ind, col_ind)
print(cost[row_ind, col_ind].sum())
