#!/usr/bin/env python
# -*- coding: utf-8 -*-

x = [1, 3, 5, 7, 9]
sum_squared = sum([y**2 for y in x])
print(sum_squared)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_squared = [y**2 for y in x if y % 2 == 0]
print(even_squared)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squared_cubed = [y**2 if y % 2 == 0 else y**3 for y in x]
print(squared_cubed)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squared_cubed = [y**2 if y % 2 != 0 else y**3 for y in x]
print(squared_cubed)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print({k: k**2 for k in x})

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print({k: k**2 for k in x if k % 2 == 0})
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print({k: k**2 if k % 2 == 0 else k**3 for k in x})
