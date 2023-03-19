#!/usr/bin/env python
"""
Munkreshungarian.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : munkreshungarian
# @created     : Saturday Mar 18, 2023 21:59:21 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
from munkres import Munkres  # type: ignore
from munkres import print_matrix  # type: ignore

m = Munkres()
matrix = [[5, 9, 1], [10, 3, 2], [8, 7, 4]]
indexes = m.compute(matrix)
print_matrix(matrix, msg="Lowest cost through this matrix:")
TOTAL = 0
for row, column in indexes:
    value = matrix[row][column]
    TOTAL += value
    print(f"({row}, {column}) -> {value}")
print(f"total cost: {TOTAL}")
