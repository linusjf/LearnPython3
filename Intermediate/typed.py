#!/usr/bin/env python
"""Staticallly typed code via annotations."""


def my_add(_a: int, _b: int) -> int:
    """Return sum."""
    return _a + _b


print(my_add(45, 67))
print(my_add(45.0, 67.9))
