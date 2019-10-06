#!/usr/bin/env python3
"""Spread."""


def spread(arg):
    """Return a flattened array."""
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret


print(spread([1, 2, 3, [4, 5, 6], [7], 8, 9]))
# [1,2,3,4,5,6,7,8,9]
print(spread([1, 2, 3, [4, [5, 7], 6], [7], 8, 9]))
