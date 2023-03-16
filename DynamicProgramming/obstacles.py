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
from copy import deepcopy
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


def solve_for_obstacles_dpspace(array):
    """Solve for obstacles with dp space array."""
    xpos = len(array)
    ypos = len(array[0])
    # If obstacle is at starting position
    if array[0][0]:
        return 0
    #  Initializing starting position
    array[0][0] = 1
    # first row all are '1' until obstacle
    for j in range(1, ypos):
        if array[0][j] == 0:
            array[0][j] = array[0][j - 1]
        else:
            # No ways to reach at this index
            array[0][j] = 0
    # first column all are '1' until obstacle
    for i in range(1, xpos):
        if array[i][0] == 0:
            array[i][0] = array[i - 1][0]
        else:
            # No ways to reach at this index
            array[i][0] = 0
    for i in range(1, xpos):
        for j in range(1, ypos):
            # If current cell has no obstacle
            if array[i][j] == 0:
                array[i][j] = array[i - 1][j] + array[i][j - 1]
            else:
                # No ways to reach at this index
                array[i][j] = 0
    # returning the bottom right
    # corner of Grid
    return array[xpos - 1][ypos - 1]


def solve_for_obstacles_dp(grid):
    """Solve for obstacles dp."""
    xpos = len(grid)
    ypos = len(grid[0])
    if xpos == 1 and ypos == 1 and grid[0][0] == 0:
        return 1
    if xpos == 1 and ypos == 1 and grid[0][0] == 1:
        return 0
    dparray = [[-1] * ypos for _ in range(xpos)]

    def path(array, grid, i, j):
        if i < xpos and j < ypos and grid[i][j] == 1:
            return 0
        if i == xpos - 1 and j == ypos - 1:
            return 1
        if i >= xpos or j >= ypos:
            return 0

        if array[i][j] != -1:
            return array[i][j]

        left = path(array, grid, i + 1, j)

        right = path(array, grid, i, j + 1)

        array[i][j] = left + right

        return array[i][j]

    path(dparray, grid, 0, 0)

    if dparray[0][0] == -1:
        return 0
    return dparray[0][0]


# Driver code
A = [
    ([0, 0, 0, 0, 0]),
    ([0, 1, 0, 0, 0]),
    ([0, 0, 1, 0, 0]),
    ([0, 0, 0, 1, 0]),
    ([0, 0, 0, 0, 0]),
    ([0, 0, 0, 0, 0]),
]
print(solve_for_obstacles_td(A))
print(timeit("solve_for_obstacles_td(A)", number=10000, globals=globals()))
print(solve_for_obstacles_dpspace(deepcopy(A)))
print(timeit("solve_for_obstacles_dpspace(deepcopy(A))", number=10000, globals=globals()))
print(solve_for_obstacles_dp(A))
print(timeit("solve_for_obstacles_dp(A)", number=10000, globals=globals()))
print(solve_for_obstacles(tuple(map(tuple, A))))
print(timeit("solve_for_obstacles(tuple(map(tuple, A)))", number=10000, globals=globals()))
