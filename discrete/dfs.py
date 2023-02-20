#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy

# Depth First Search
#
# INPUTS
# A - an adjacency matrix. It should be square, symmetric, and
# binary
# source - the number of the source vertex
#
# OUTPUTS
# vertexList - an ordered list of vertices found in the search


def DFS(A, source):
    # reduce the source by 1 to avoid off-by-1 errors
    source -= 1

    # find the number of vertices
    n = A.shape[0]

    # initialize the unvisited vertex set to be full
    unvisited = [1] * n

    # initialize a queue with the source vertex
    stack = [source]

    # initialize the vertex list
    vertexList = []

    # while the stack is not empty
    while stack:
        # remove the just-visited vertex from the stack and
        # store it
        v = stack.pop()

        # if v is unvisited, add it to our list and mark it as
        # visited
        if unvisited[v]:
            # save and print the number of the newly visited
            # vertex
            vertexList.append(v)

            # mark the vertex as visited
            unvisited[v] = 0
            # iterate through the vertices
            for u in range(n - 1, 0, -1):
                # add each unvisited neighbor to the stack
                if A[v, u] == 1 and unvisited[u] == 1:
                    stack.append(u)

    return vertexList


# Save the adjacency matrix for the graph in Figure 9.1
A = numpy.array(
    [
        [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
)
# Run DFS on the graph with adjacency matrix A and source 1
vertexList = DFS(A, 1)
# Add 1 to the vertex numbers
print([x + 1 for x in vertexList])
