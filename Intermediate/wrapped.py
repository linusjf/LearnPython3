#!/usr/bin/env python3
"""Wrapped Iterator."""
from locked import LockedIterator

GEN = [x * 2 for x in [1, 2, 3, 4]]

for _ in GEN:
    print(_)

G2 = LockedIterator(GEN)
for _ in G2:
    print(_)
