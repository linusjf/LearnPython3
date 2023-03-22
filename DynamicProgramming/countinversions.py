#!/usr/bin/env python
"""
Countinversions.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : countinversions
# @created     : Wednesday Mar 22, 2023 19:56:23 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
from heapq import heappush, heappop
from bisect import bisect, insort


class Solution:  # pylint: disable=too-few-public-methods
    """Solve inversion count."""

    def count_inversions(self, input_arr):
        """Count inversions."""
        print(f"input_arr = {input_arr}")
        arr, result = [], 0
        # Push elements (A[i], i) in a heap to get a sorted array.
        for i, elem in enumerate(input_arr):
            heappush(arr, (elem, i))
        indexes = []
        while len(arr) > 0:
            print(f"arr = {arr}")
            # Pop the minimum element from the heap.
            _, i = heappop(arr)
            print(f"_, i = {_}, {i}")
            # Find the position to insert in the array index.
            # bisect function in python will calculate this in O(log(N)) time
            j = bisect(indexes, i)
            print(f"j = {j}")
            # Add number of elements that have index greater in original array
            # input_arr.
            print("result += len(indexes) - j")
            result += len(indexes) - j
            print(f"result = {result}")
            # Insert the index of current element in the array index in sorted
            # manner.
            insort(indexes, i)
            print(f"indexes = {indexes}")
        return result


# Driver Code
# Given array is
ARR = [1, 20, 6, 4, 5]
res = Solution().count_inversions(ARR)
print("Number of inversions are: ", res)
ARR = [5, 3, 2, 4, 1]
res = Solution().count_inversions(ARR)
print("Number of inversions are: ", res)
