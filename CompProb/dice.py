#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
pmf of sum of two die
"""
# start with empty pmf
pmf = {}  
for x in range(1, 7):
    for y in range(1, 7):
        if (x+y) in pmf:
            pmf[x+y] += 1/36
        else:
            pmf[x+y] = 1/36
print(pmf)
