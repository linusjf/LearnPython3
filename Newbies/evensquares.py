#!/usr/bin/env python
"""Print squares of even numbers."""
EVEN_SQUARES = [x * x for x in range(10) if not x % 2]
print(EVEN_SQUARES)
