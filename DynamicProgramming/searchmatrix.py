#!/usr/bin/env python
"""
Searchmatrix.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : searchmatrix
# @created     : Monday Mar 27, 2023 19:36:20 IST
# @description :
# Python3 program for implementation of
# divide and conquer algorithm to find
# a given key in a row-wise and column-wise
# sorted 2D array a divide and conquer method
# to search a given key in mat in rows from
# from_row to to_row and columns from from_col to
# to_col
# https://www.geeksforgeeks.org/search-in-a-row-wise-and-column-wise-sorted-2d-array-using-divide-and-conquer-algorithm/
# -*- coding: utf-8 -*-'
######################################################################
"""


def search(mat, bounds, key):
    """Find middle and compare with middle."""
    from_row, to_row, from_col, to_col = bounds
    i = from_row + (to_row - from_row) // 2
    j = from_col + (to_col - from_col) // 2
    if mat[i][j] == key:
        # If key is present at middle
        print(f"Found {key} at {i},{j}")
    else:
        # right-up quarter of matrix is searched in all cases.
        # Provided it is different from current call
        if i != to_row or j != from_col:
            search(mat, (from_row, i, j, to_col), key)
        # Special case for iteration with 1*2 matrix
        # mat[i][j] and mat[i][j+1] are only two elements.
        # So just check second element
        if from_row == to_row and from_col + 1 == to_col:
            if mat[from_row][to_col] == key:
                print(f"Found {key} at {from_row},{to_col}")
        # If middle key is lesser then search lower horizontal
        # matrix and right hand side matrix
        if mat[i][j] < key:
            # search lower horizontal if such matrix exists
            if i + 1 <= to_row:
                search(mat, (i + 1, to_row, from_col, to_col), key)
        # If middle key is greater then search left vertical
        # matrix and right hand side matrix
        else:
            # search left vertical if such matrix exists
            if j - 1 >= from_col:
                search(mat, (from_row, to_row, from_col, j - 1), key)


if __name__ == "__main__":
    MAT = [[10, 20, 30, 40], [15, 25, 35, 45], [27, 29, 37, 48], [32, 33, 39, 50]]
    ROWCOUNT = len(MAT)
    COLCOUNT = len(MAT[0])
    KEY = 50
    search(MAT, (0, ROWCOUNT - 1, 0, COLCOUNT - 1), KEY)
    for idx in range(0, ROWCOUNT):
        for jdx in range(0, COLCOUNT):
            search(MAT, (0, ROWCOUNT - 1, 0, COLCOUNT - 1), MAT[idx][jdx])
