#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

text = """
I need to count the number of word
occurrences in a piece of text. How could I do that?
Python provides us with multiple ways to do the same
thing. But only one way I find beautiful.
"""
word_count_dict = {}
words = re.split("\s|(?<!\d)[,.?](?!\d)", text)
gen = (w for w in words if len(w) > 0)
for w in gen:
    if w in word_count_dict:
        word_count_dict[w] += 1
    else:
        word_count_dict[w] = 1

print(word_count_dict)

from collections import defaultdict

gen = (w for w in words if len(w) > 0)
word_count_dict = defaultdict(int)
for w in gen:
    word_count_dict[w] += 1
print(word_count_dict)

from collections import Counter

gen = (w for w in words if len(w) > 0)
word_count_dict = Counter()
for w in gen:
    word_count_dict[w] += 1
print(word_count_dict)
print(word_count_dict.most_common(10))

# Count Characters
print(Counter("abccccccddddd"))
# Count List elements
print(Counter([1, 2, 3, 4, 5, 1, 2]))

s = [
    ("color", "blue"),
    ("color", "orange"),
    ("color", "yellow"),
    ("fruit", "banana"),
    ("fruit", "orange"),
    ("fruit", "banana"),
]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
print(d)
d = defaultdict(set)
for k, v in s:
    d[k].add(v)
print(d)
