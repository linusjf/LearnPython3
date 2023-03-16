#!/usr/bin/env python
"""
Obstacles.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : obstacles
# @created     : Wednesday Mar 15, 2023 21:15:17 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
from timeit import timeit
from functools import lru_cache


@lru_cache
def unique_paths(i, j, array):
    """Solve for unique paths."""
    posx, posy = len(array), len(array[0])
    # boundary condition or constraints
    if i == posx or j == posy:
        return 0
    if array[i][j] == 1:
        return 0

    if i == posx - 1 and j == posy - 1:
        return 1
    return sum([unique_paths(i + 1, j, array), unique_paths(i, j + 1, array)])


def unique_paths_td(i, j, array, paths=None):
    """Solve for unique paths top-down."""
    posx, posy = len(array), len(array[0])
    # boundary condition or constraints
    if i == posx or j == posy:
        return 0
    if array[i][j] == 1:
        return 0

    if i == posx - 1 and j == posy - 1:
        return 1
    if paths is None:
        paths = [[-1] * posy for _ in range(posx)]
    if paths[i][j] != -1:
        return paths[i][j]
    paths[i][j] = unique_paths_td(i + 1, j, array, paths) + unique_paths_td(i, j + 1, array, paths)
    return paths[i][j]


def solve_for_obstacles(array):
    """Solve for obstacles."""
    return unique_paths(0, 0, array)


def solve_for_obstacles_td(array):
    """Solve for obstacles."""
    return unique_paths_td(0, 0, array)


# Driver code
A = [
    tuple([0, 0, 0, 0, 0]),
    tuple([0, 1, 0, 0, 0]),
    tuple([0, 0, 1, 0, 0]),
    tuple([0, 0, 0, 1, 0]),
    tuple([0, 0, 0, 0, 0]),
    tuple([0, 0, 0, 0, 0]),
]
print(solve_for_obstacles(tuple(A)))
print(timeit("solve_for_obstacles(tuple(A))", number=10000, globals=globals()))
print(solve_for_obstacles_td(tuple(A)))
print(timeit("solve_for_obstacles_td(tuple(A))", number=10000, globals=globals()))
