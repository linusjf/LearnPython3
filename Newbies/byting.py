#!/usr/bin/env python3
"""Size in bytes."""


def byte_size(string):
    """Return size in bytes."""
    return len(string.encode("utf-8"))


print(byte_size("😀"))
print(byte_size("Hello World"))
