#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Sets example using python
"""
sample_space = {'HH', 'HT', 'TH', 'TT'}
A = {'HT', 'TT'}
B = {'HH', 'HT', 'TH'}
C = {'HH'}
# equivalent to "B.intersection(A)" or "A & B"
A_intersect_B = A.intersection(B) 
print(A_intersect_B)
# equivalent to "C.union(A)" and also "A | C"
A_union_C = A.union(C)  
print(A_union_C)
# equivalent also to "sample_space - B"
B_complement = sample_space.difference(B)  
print(B_complement)

faces_that_add_to_7 = set()
for x in range(1, 7):
    for y in range(1, 7):
        if x + y == 7:
            faces_that_add_to_7.add((x, y))

print(faces_that_add_to_7)
