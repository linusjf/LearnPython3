#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import numpy as np

x = [3,4]
# magnitude of a vector
print(np.linalg.norm(x))

# Compute the direction of a vector x.
def direction(x):
 return x/np.linalg.norm(x)

print(direction(x))

u_1 = np.array([3,4])
u_2 = np.array([30,40])
# [0.6 , 0.8]
print(direction(u_1)) 
# [0.6 , 0.8]
print(direction(u_2))

# norm of direction vector is always 1.0
# unit vector
print(np.linalg.norm(np.array([0.6, 0.8])))

def geometric_dot_product(x,y, theta):
    x_norm = np.linalg.norm(x)
    y_norm = np.linalg.norm(y)
    return x_norm * y_norm * math.cos(math.radians(theta))

theta = 45 
x = [3,5]
y = [8,2]
# 34.0
print(geometric_dot_product(x,y,theta))

def dot_product(x,y):
    result = 0
    for i in range(len(x)):
        result = result + x[i]*y[i]
    return result

# 34.0
print(dot_product(x,y))

# numpy function
x = np.array([3,5])
y = np.array([8,2])
# 34
print(np.dot(x,y)) 
