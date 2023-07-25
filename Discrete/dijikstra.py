#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy


# Use the previousVertices chart to construct the shortest path
# from input source to input destination and print a
# string showing the path
def printShortestPath(shortestDistances, previousVertices, source, destination):
    # avoid off-by-one error
    source -= 1
    destination -= 1

    # convert previousVertices to integers
    previousVertices = previousVertices.astype(int)

    # initialize the path with the destination
    path = [destination]

    # add the previous vertex from previousVertices until we
    # reach the source
    # the source
    for _ in range(previousVertices.shape[0] - 1):
        # if the source is in the path, stop
        if path[-1] == source:
            break
        # if the source is not in the path, add the previous vertex
        else:
            path.append(previousVertices[path[-1]])

    # initialize an output string
    output = []

    # iterate through the path backwards (source to destination)
    for i in numpy.flip(path):
        # construct a list of strings to output
        if i > 0:
            output.append("->")
        output.append("v" + str(i + 1))

    # print the strings with no spaces
    print("Path =", *output, "\nDistance =", shortestDistances[destination])


# Dijkstra's algorithm for finding shortest paths from the
# source vertex to all other vertices in the graph
#
# INPUTS
# W - a weight matrix. It should be a square matrix
# i - the number of the source node
#
# OUTPUTS
# shortestDistances - the shortest distances from the source to
# each vertex
# previousVertices - the previous vertex to the destination in
# shortest path from the source to a destination


def Dijkstra(W, i):
    # find the number of vertices
    n = W.shape[0]

    # initialize the shortest distances to infinity
    shortestDistances = numpy.array([numpy.inf] * n)

    # initialize the previous vertices
    previousVertices = numpy.array([numpy.inf] * n)

    # initialize the unvisited vertex set to be full
    unvisited = numpy.array([1] * n)

    # mark the source as visited
    unvisited[i - 1] = 0
    # initialize distance from the source to the source as 0
    shortestDistances[i - 1] = 0

    # loop for iteration per vertex until the unvisited set is
    # empty
    for _ in range(n):
        # find the distances to all unvisited adjacent vertices
        # and set others to 0
        distances = shortestDistances * unvisited
        # find the index of the nearest unvisited vertex (where
        # distances > 0)
        x = numpy.argmin(numpy.ma.masked_where(distances == 0, distances))

        # mark vertex x as visited
        unvisited[x] = 0
        # iterate through the vertices
        for v in range(n):
            oldDistance = shortestDistances[v]
            newDistance = shortestDistances[x] + W[v, x]
            adjacent = W[v, x] > 0
            unvis = unvisited[v]
            # if v and x are connected, v has not been visited,
            # and we find a shorter distance to node v...
            if adjacent and unvis and oldDistance > newDistance:
                # save the shortest distance found so far
                shortestDistances[v] = newDistance
                # save the previous vertex
                previousVertices[v] = x

    # print the table similar to the book
    print(numpy.array([numpy.arange(n) + 1, shortestDistances, previousVertices + 1]).T)
    # return the outputs
    return shortestDistances, previousVertices


# find the shortest paths to connected vertices
def distancesWithinComponent(source):
    # initialize the connected component
    component = [source]
    # construct the connected component
    for i in range(1, W2.shape[0] + 1):
        if i != source and isConnected(W2, source, i):
            component.append(i)

    print("component = ", component)
    # find the weight matrix correponding to the connected component
    subnetwork = W2[numpy.array(component) - 1, :][:, numpy.array(component) - 1]
    # run Dijkstra's algorithm
    return Dijkstra(subnetwork, 1)


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


# Create a weight matrix for the network in Figure 9.15
W1 = numpy.array(
    [
        [0, 4, 1, 0, 2, 0],
        [4, 0, 2, 1, 0, 1],
        [1, 2, 0, 1, 1, 0],
        [0, 1, 1, 0, 2, 0],
        [2, 0, 1, 2, 0, 0],
        [0, 1, 0, 0, 0, 0],
    ]
)

# Run Dijkstra's algorithm with a source at vertex v1
s, p = Dijkstra(W1, 1)
print(s, p)
for i in range(2, 7):
    printShortestPath(s, p, 1, i)

# Create a weight matrix for the network in Figure 9.16
W2 = numpy.array(
    [
        [0, 4, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 4, 0],
        [0, 0, 1, 0, 2, 0],
        [0, 0, 4, 2, 0, 0],
        [0, 1, 0, 0, 0, 0],
    ]
)

s, p = distancesWithinComponent(1)
print(s, p)
for i in range(2, s.shape[0] + 1):
    printShortestPath(s, p, 1, i)
s, p = distancesWithinComponent(3)
print(s, p)
for i in range(2, s.shape[0] + 1):
    printShortestPath(s, p, 1, i)
