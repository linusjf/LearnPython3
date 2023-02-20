#!/usr/bin/env python
"""
######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : scarlet
# @created     : Sunday Feb 05, 2023 18:12:23 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import urllib.request
import re

SCARLET_PIMPERNEL_LINK = r"https://www.gutenberg.org/cache/epub/60/pg60.txt"
word1 = re.compile(rb"\bthe\b")
word2 = re.compile(rb"\bis\b")
_COUNT = 0
with urllib.request.urlopen(SCARLET_PIMPERNEL_LINK) as ip_file:
    for line in ip_file:
        print(line)
        if word1.search(line) or word2.search(line):
            _COUNT += 1
print(_COUNT)
