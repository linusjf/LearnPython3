#!/usr/bin/env python
# -*- coding: utf-8 -*-
 # Transform a two-dimensional vector x into a three-dimensional vector.

def transform(x):
    return [x[0]**2, np.sqrt(2)*x[0]*x[1], x[1]**2]
