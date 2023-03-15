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


def unique_paths(i, j, posx, posy, array):
    """Solve for unique paths."""
    # boundary condition or constraints
    if i == posx or j == posy:
        return 0
    if array[i][j] == 1:
        return 0

    if i == posx - 1 and j == posy - 1:
        return 1
    return sum(
        [unique_paths(i + 1, j, posx, posy, array), unique_paths(i, j + 1, posx, posy, array)]
    )


def solve_for_obstacles(array):
    """Solve for obstacles."""
    xpos, ypos = len(array), len(array[0])
    return unique_paths(0, 0, xpos, ypos, array)


# Driver code
A = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
print(solve_for_obstacles(A))
