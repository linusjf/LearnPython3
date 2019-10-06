#!/usr/bin/env python3
"""Check for uniqueness in set."""
def all_unique(lst):
    """Returns whether list is unique."""
    return len(lst) == len(set(lst))


X = [1, 1, 2, 2, 3, 2, 3, 4, 5, 6]
Y = [1, 2, 3, 4, 5]
print(all_unique(X))
print(all_unique(Y))
