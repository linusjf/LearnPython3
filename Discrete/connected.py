#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy


# create a function that returns True if vertex i and vertex j
# are connected in the graph represented by the input
# adjacency matrix A
def isConnected(A, i, j):
    # initialize the paths matrix to adjacency matrix A
    paths = A

    # find the number of vertices in the graph
    numberOfVertices = A.shape[0]

    # find the number of edges in the graph
    numberOfEdges = numpy.sum(A) / 2
    # if vi and vj are adjacent, return True
    if paths[i - 1][j - 1] > 0:
        print("Vertex", i, "and vertex", j, "are adjacent")
        return True
    else:
        # run the loop until we find a path
        for pathLength in range(2, numberOfVertices):
            # exponentiate the adjacency matrix
            paths = numpy.dot(paths, A)
            # if the element in row i, column j is more than 0,
            # we found a path
            if paths[i - 1][j - 1] > 0:
                print("There is a path with", pathLength, "edges from vertex", i, "to vertex", j)
                return True

    # found no paths, the vertices are not connected
    if pathLength == numberOfEdges:
        print("There are no paths from vertex", i, "to vertex", j)
        return False


# create an adjacency matrix for the graph G1
A1 = numpy.array(
    [
        [0, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 0, 1],
        [1, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 0, 0],
        [0, 1, 0, 0, 0, 0],
    ]
)
# check if various vertices are connected
print(isConnected(A1, 1, 4))
print(isConnected(A1, 2, 3))
print(isConnected(A1, 5, 6))

print()

# create an adjacency matrix for graph G2
A2 = numpy.array(
    [
        [0, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 1, 0, 0, 0, 0],
    ]
)
print(isConnected(A2, 1, 6))
print(isConnected(A2, 2, 5))
print(isConnected(A2, 1, 4))
