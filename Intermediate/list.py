#!/usr/bin/env python
"""Python's list slice syntax can be used without indices."""

LST = [1, 2, 3, 4, 5]
del LST[:]
print(LST)

# You can replace all elements of a list
# without creating a new list object:
A = LST
LST[:] = [7, 8, 9]
print(LST)
print(A)
print(A is LST)

# You can also create a (shallow) copy of a list:
B = LST[:]
print(B)
print(B is LST)
