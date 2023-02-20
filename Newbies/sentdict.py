#!/usr/bin/env python3
"""Creating a dictionary from sentence."""
import re

STRING = """Creating a dictionary and updating it with word count.
We will discuss other methods of updating a dictionary later."""

TOKENS = re.split(r"[\s\.\n]\s*", STRING)

COUNT = {}

for WORD in TOKENS:
    if WORD:
        COUNT[WORD] = COUNT.get(WORD, 0) + 1

print(COUNT)
