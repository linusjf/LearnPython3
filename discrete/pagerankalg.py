#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
# The PageRank algorithm for ranking search results
#
# INPUTS
# A - the transition probability matrix
# d - the damping factor, default = 0.85
# eps - the error threshold, default = 0.0005
# maxIterations - the maximum iterations it can run before stopping
# verbose - if true, the algorithm prints the progress of PageRank
# 
# OUTPUTS
# vNew - the steady state PageRank vector
def PageRank(A, d = 0.85, eps = 0.0005, maxIterations = 1000,
 verbose = False):
    # find the size of the "Internet"
    N = A.shape[0]

    # initialize the old and new PageRank vectors
    vOld = numpy.ones([N])
    vNew = numpy.ones([N])/N
    # initialize a counter
    i = 0
    # compute the update matrix
    U = d * A.T + (1 - d) / N
 
    while numpy.linalg.norm(vOld - vNew) >= eps:
        # if the verbose flag is true, print the progress at each iteration
        if verbose:
            print('At iteration', i, 'the error is',
              numpy.round(numpy.linalg.norm(vOld - vNew), 3), 
              'with PageRank', numpy.round(vNew, 3))

        # save the current PageRank as the old PageRank
        vOld = vNew

        # update the PageRank vector
        vNew = numpy.dot(U, vOld)

        # increment the counter
        i += 1
# if it runs too long before converging, stop and notify the user
        if i == maxIterations:
            print('The PageRank algorithm ran for',
                  maxIterations, 'with error',
                  numpy.round(numpy.linalg.norm(vOld - vNew), 
                              3))
            # return the PageRank vector and the 
            return vNew, i

    # return the steady state PageRank vector and iteration number
    return vNew, i

# transition probability matrix
A = numpy.array([[0, 1/4, 1/4, 1/4, 1/4],
 [1/2, 0, 0, 1/2, 0],
 [1/3, 0, 0, 1/3, 1/3],
 [1, 0, 0, 0, 0],
 [0, 0, 0, 1, 0]])
# Run the PageRank algorithm with default settings
print(PageRank(A, verbose=True))

# transition probability matrix
B = numpy.array([[0, 1/4, 1/4, 1/4, 1/4],
 [1/3, 0, 1/3, 1/3, 0],
 [1/3, 0, 0, 1/3, 1/3],
 [1/2, 0, 1/2, 0, 0],
 [0, 0, 1/2, 1/2, 0]])
# Run the PageRank algorithm with default settings
print(PageRank(B, verbose = True))

# import the pandas library
import pandas
# read the txt file into a dataframe
data = pandas.read_csv("California.txt", delimiter=' ')
# display the dataframe
print(data)

# preprocess the data
# select only the rows with type 'e'
adjacencies = data.loc[data['Type'] == 'e']
# drop the 'Type' column
adjacencies = adjacencies.drop(columns = 'Type')
# convert the adjacency list to a NumPy array
adjacencies = adjacencies.to_numpy()

# convert the adjacency list to integers
adjacencies = adjacencies.astype('int')
# print the adjacency list
print(adjacencies)

# convert the adjacency list to an adjacency matrix
# find the number of webpages and initialize A
N = numpy.max(adjacencies) + 1
A = numpy.zeros([N, N])
# iterate over the rows of the adjacency list
for k in range(adjacencies.shape[0]):
    # find the adjacent vertex numbers
    i, j = adjacencies[k,]

    # put 1 in the adjacency matrix
    A[i, j] = 1

# convert A to the transition probability matrix
# divide each row of A by its row sum
rowSums = A.sum(axis = 1)[:,None]
# divide A by the rowSums
A = numpy.divide(A, rowSums, where = rowSums != 0)
# run PageRank
v, i = PageRank(A,verbose=True)
# print the steady state PageRank vector and iteration number
print(v)
print(i)
