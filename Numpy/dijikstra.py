#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy
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
        x = numpy.argmin(numpy.ma.masked_where(
            distances == 0, distances))

        # mark vertex x as visited
        unvisited[x] = 0
        # iterate through the vertices
        for v in range(n):
            oldDistance = shortestDistances[v]
            newDistance = shortestDistances[x] + W[v,x]
            adjacent = W[v,x] > 0
            unvis = unvisited[v]
            # if v and x are connected, v has not been visited, 
            # and we find a shorter distance to node v...
            if adjacent and unvis and oldDistance > newDistance:
                # save the shortest distance found so far
                shortestDistances[v] = newDistance
                # save the previous vertex
                previousVertices[v] = x
        
    # print the table similar to the book
    print(numpy.array([numpy.arange(n) + 1, shortestDistances,previousVertices + 1]).T)
    # return the outputs
    return shortestDistances, previousVertices

# Create a weight matrix for the network in Figure 9.15
W1 = numpy.array([[0, 4, 1, 0, 2, 0],
 [4, 0, 2, 1, 0, 1],
 [1, 2, 0, 1, 1, 0],
 [0, 1, 1, 0, 2, 0],
 [2, 0, 1, 2, 0, 0],
 [0, 1, 0, 0, 0, 0]])

# Run Dijkstra's algorithm with a source at vertex v1
s,p = Dijkstra(W1, 1)
print(s,p)
