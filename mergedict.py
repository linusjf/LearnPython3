#!/usr/bin/env python3
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

z = {**x, **y}
print(z)
z = {**y, **x}
print(z)
