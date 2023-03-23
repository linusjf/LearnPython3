#!/usr/bin/env python
"""
Skylineheap.

######################################################################
# @author      : ChatGPT
# @file        : skylineheap
# @created     : Thursday Mar 23, 2023 20:31:21 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import heapq


# pylint: disable=invalid-name
def get_skyline(buildings):
    """
    Solves the Skyline problem using a heap-based algorithm.

    Returns a list of (x, height) tuples representing the skyline.
    """
    skyline = []
    heap = []
    i = 0
    n = len(buildings)

    while i < n or heap:
        if not heap or (i < n and buildings[i][0] <= -heap[0][1]):
            x = buildings[i][0]
            while i < n and buildings[i][0] == x:
                heapq.heappush(heap, (-buildings[i][2], -buildings[i][1]))
                i += 1
        else:
            x = -heap[0][1]
            while heap and -heap[0][1] <= x:
                heapq.heappop(heap)
        height = len(heap) and -heap[0][0]
        if not skyline or height != skyline[-1][1]:
            skyline.append((x, height))

    return skyline


ARR = [
    (1, 5, 11),
    (2, 7, 6),
    (3, 9, 13),
    (12, 16, 7),
    (14, 25, 3),
    (19, 22, 18),
    (23, 29, 13),
    (24, 28, 4),
]
print(get_skyline(ARR))
