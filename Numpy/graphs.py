#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy 
# Create an adjacency matrix for the graph in Figure 8.1
A1 = numpy.array([[0, 1, 1, 0, 1, 0], [1, 0, 1, 1, 0, 1],
 [1, 1, 0, 1, 1, 0], [0, 1, 1, 0, 1, 0],
 [1, 0, 1, 1, 0, 0], [0, 1, 0, 0, 0, 0]])
# Create an adjacency matrix for the graph in Figure 8.8
A2 = numpy.array([[0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 1],
 [0, 0, 0, 1, 1, 0], [0, 0, 1, 0, 1, 0],
 [0, 0, 1, 1, 0, 0], [0, 1, 0, 0, 0, 0]])
# Create an adjacency matrix for the directed graph in Figure 
 # 8.6
A3 = numpy.array([[0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 0, 1],
 [0, 0, 0, 0, 1, 0], [0, 1, 1, 0, 1, 0],
 [1, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1]])
# print the adjacency matrices
print("A1 =", A1)
print("\n A2 =", A2)
print("\n A3 =", A3)

# Create a weight matrix for the network in Figure 8.5
W1 = numpy.array([[0, 4, 1, 0, 2, 0], [4, 0, 2, 1, 0, 1],
 [1, 2, 0, 1, 1, 0], [0, 1, 1, 0, 2, 0],
 [2, 0, 1, 2, 0, 0], [0, 1, 0, 0, 0, 0]])
# Create a weight matrix for the directed network in Figure 8.7
W2 = numpy.array([[0, 0, 2, 0, 0, 0], [1, 0, 0, 0, 0, 2],
 [0, 0, 0, 0, 2, 0], [0, 2, 3, 0, 4, 0],
 [3, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1]])
# Print the weight matrices
print("W1 =", W1)
print("\n W2 =", W2)

# Find the degrees of each vertex of the graph in Figure 8.1
# Using column sums
print(numpy.sum(A1, axis=0))
# Using row sums
print(numpy.sum(A1, axis=1))

# Find out-degrees for each vertex in the directed graph in 
 # Figure 8.6
outdegrees = numpy.sum(A3, axis=1)
print(outdegrees)
# Find in-degrees for each vertex in the directed graph in 
 # Figure 8.6
indegrees = numpy.sum(A3, axis=0)
print(indegrees)
print(numpy.sum(outdegrees))
print(numpy.sum(indegrees))

# Find the second power of adjacency matrix A1
print("A1² = ",numpy.linalg.matrix_power(A1,2))
# Find the third power of adjacency matrix A1
print("\nA1³ = ", numpy.linalg.matrix_power(A1,3))
