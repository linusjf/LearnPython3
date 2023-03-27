#!/usr/bin/env python
"""
Search Matrix Binary.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : searchmatrixbin
# @created     : Monday Mar 27, 2023 21:10:26 IST
# @description :
# https://www.geeksforgeeks.org/search-in-a-row-wise-and-column-wise-sorted-2d-array-using-divide-and-conquer-algorithm/
# -*- coding: utf-8 -*-'
######################################################################
"""


def binary_search(mat, row, start, end, key):
    """Search binary."""
    while start <= end:
        mid = start + (end - start) // 2
        if mat[row][mid] == key:
            return True
        if mat[row][mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return False


def search(mat, key):
    """Search for key."""
    rows = len(mat)
    cols = len(mat[0])
    # search in each row
    for i in range(rows):
        # perform binary search in current row
        if key in range(mat[i][0], mat[i][cols - 1] + 1):
            if binary_search(mat, i, 0, cols - 1, key):
                print(f"Found {key} at {i}")
                return
    print(f"{key} not found")


# Driver code
def main():
    """Execute main."""
    mat = [[10, 20, 30, 40], [15, 25, 35, 45], [27, 29, 37, 48], [32, 33, 39, 50]]
    key = 50
    search(mat, key)


if __name__ == "__main__":
    main()
