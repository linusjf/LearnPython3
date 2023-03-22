#!/usr/bin/env python
"""
Subarray.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : subarray
# @created     : Wednesday Mar 22, 2023 13:20:24 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
NOT_POSSIBLE = "Not possible"
# O(n) solution for finding smallest
# subarray with sum greater than x
# Returns length of smallest subarray
# with sum greater than x. If there
# is no subarray with given sum, then
# returns n + 1


def smallest_sub_with_sum(arr, xval):
    """Compute smallest subarray with sliding window approach."""
    size = len(arr)
    # Initialize current sum and minimum length
    curr_sum = 0
    min_len = size + 1
    # Initialize starting and ending indexes
    start = 0
    end = 0
    while end < size:
        # Keep adding array elements while current
        # sum is smaller than or equal to x
        while curr_sum <= xval and end < size:
            curr_sum += arr[end]
            end += 1
        # If current sum becomes greater than x.
        while curr_sum > xval and start < size:
            # Update minimum length if needed
            if end - start < min_len:
                min_len = end - start
            # remove starting elements
            curr_sum -= arr[start]
            start += 1
    return min_len


# Driver program
arr1 = [1, 4, 45, 6, 10, 19]
X = 51
res1 = smallest_sub_with_sum(arr1, X)
if res1 == len(arr1) + 1:
    print(NOT_POSSIBLE)
else:
    print(res1)

arr2 = [1, 10, 5, 2, 7]
X = 9
res2 = smallest_sub_with_sum(arr2, X)
if res2 == len(arr2) + 1:
    print(NOT_POSSIBLE)
else:
    print(res2)
arr3 = [1, 11, 100, 1, 0, 200, 3, 2, 1, 250]
X = 280
res3 = smallest_sub_with_sum(arr3, X)
if res3 == len(arr3) + 1:
    print(NOT_POSSIBLE)
else:
    print(res3)
