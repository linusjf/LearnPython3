#!/usr/bin/env python3
"""Anagrams."""
from collections import Counter

def anagram(first, second):
    """Returns whether second is anagram of first."""
    return Counter(first) == Counter(second)


print(anagram("abcd3", "3acdb"))
print(Counter("abcd3"))
print(Counter("3acdb"))
