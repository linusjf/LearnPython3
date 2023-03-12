#!/usr/bin/env python
"""
Floydwarshall.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : floydwarshall
# @created     : Sunday Mar 12, 2023 12:10:56 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import sys

# Floyd Warshall Algorithm in python
INF = sys.maxsize


# Algorithm implementation
def floyd_warshall(graph):
    """Solve Floyd Warshall."""
    distance = list(map(lambda i: list(map(lambda j: j, i)), graph))
    vertices = len(graph)
    # Adding vertices individually
    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print_solution(vertices, distance)


# Printing the solution
def print_solution(vertices, distance):
    """Print solution."""
    for i in range(vertices):
        for j in range(vertices):
            if distance[i][j] == INF:
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


GRAPH = [[0, 3, INF, 5], [2, 0, INF, 4], [INF, 1, 0, INF], [INF, INF, 2, 0]]
floyd_warshall(GRAPH)
