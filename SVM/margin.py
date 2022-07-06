#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

# Compute the functional margin of an example (x,y)
# with respect to a hyperplane defined by w and b.
def example_functional_margin(w, b, 
x, y):
    result = y * (np.dot(w, x) + b)
    return result

# Compute the functional margin of a hyperplane
# for examples X with labels y.
def functional_margin(w, b, X, y):
    return np.min([example_functional_margin(w, b, x, y[i])
                   for  i, x in enumerate(X)])

x = np.array([1, 1])
y = 1
b_1 = 5
w_1 = np.array([2, 1])
w_2 = w_1 * 10

b_2 = b_1 * 10

# 8
print (example_functional_margin(w_1, b_1, x, y))
# 80
print (example_functional_margin(w_2, b_2, x, y)) 
y = -1
# -8
print (example_functional_margin(w_1, b_1, x, y))
# -80
print (example_functional_margin(w_2, b_2, x, y))

# Compute the geometric margin of an example (x,y)
# with respect to a hyperplane defined by w and b.
def  example_geometric_margin(w, b, 
x, y):

     norm = np.linalg.norm(w)
     result = y * (np.dot(w/norm, x)+ b/norm)
     return  result

# Compute the geometric margin of a hyperplane

 # for examples X with labels y.
def  geometric_margin(w, b, X, y):
    return  np.min([example_geometric_margin(w, b, x, y[i])
                    for  i, x in enumerate(X)])


y = 1
# 3.577708764
print (example_geometric_margin(w_1, b_1, x, y))  
# 3.577708764
print(example_geometric_margin(w_2, b_2, x, y))  
y = -1
# -3.577708764
print (example_geometric_margin(w_1, b_1, x, y))  
# -3.577708764
print(example_geometric_margin(w_2, b_2, x, y)) 

# Compare two hyperplanes using the geometrical margin.
positive_x = [[2,7],[8,3],[7,5],[4,4],[4,6],[1,3],[2,5]]

negative_x = [[8,7],[4,10],[9,7],[7,10],[9,6],[4,8],[10,10]]

X = np.vstack((positive_x, negative_x))

y = np.hstack((np.ones(len(positive_x)), 
               -1*np.ones(len(negative_x))))

w = np.array([-0.4, -1])

b = 8

# 0.185695338177
print(geometric_margin(w, b, X, 
y))          
# change the value of b
# 0.64993368362
print(geometric_margin(w, 8.5, X, 
y))        
