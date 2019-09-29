#!/usr/bin/env python3
"""Infinite looper with send."""


def infinite_looper(objects):
    """Loop indefinitely."""
    count = 0
    while True:
        if count >= len(objects):
            count = 0
        message = yield objects[count]
        if message is not None:
            count = 0 if message < 0 else message
        else:
            count += 1


X = infinite_looper("A string with some words")
print(next(X))
print(X.send(9))
print(X.send(12))
print(X.send(-10))
