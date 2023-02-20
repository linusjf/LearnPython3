#!/usr/bin/env python
# -*- coding: utf-8 -*-
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in a:
    print(row[0])
for row in a:
    for element in row:
        print(element)
for i in range(3):
    print(a[i][i])
for i in range(3):
    print(f"The {i + 1}-th diagonal element is: {a[i][i]}")
