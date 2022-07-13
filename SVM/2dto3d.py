#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
# Transform a two-dimensional vector x into a three-dimensional vector.

def transform(x):
    return [x[0]**2, np.sqrt(2)*x[0]*x[1], x[1]**2]

x1 = [3,6]

x2 = [10,10]

x1_3d = transform(x1)

x2_3d = transform(x2)

# 8100
print (np.dot(x1_3d,x2_3d))  
