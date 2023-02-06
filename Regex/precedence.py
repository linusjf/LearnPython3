#!/usr/bin/env python
"""
######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : precedence
# @created     : Monday Feb 06, 2023 11:14:29 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import re

WORDS = 'lion elephant are rope not'
# span shows the start and end+1 index of matched portion
# match shows the text that satisfied the search criteria
print(re.search(r'on', WORDS))
print(re.search(r'ant', WORDS))
# starting index of 'on' < index of 'ant' for given string input
# so 'on' will be replaced irrespective of order
# count optional argument here restricts no. of replacements to 1
print(re.sub(r'on|ant', r'X', WORDS, count=1))
print(re.sub(r'ant|on', r'X', WORDS, count=1))

MOOD = 'best years'
print(re.search(r'year', MOOD))
print(re.search(r'years', MOOD))
# starting index for 'year' and 'years' will always be same
# so, which one gets replaced depends on the order of alternation
print(re.sub(r'year|years', r'X', MOOD, count=1))
print(re.sub(r'years|year', r'X', MOOD, count=1))

WORDS = 'ear xerox at mare part learn eye'
# this is going to be same as: r'ar'
print(re.sub(r'ar|are|art', r'X', WORDS))
# this is going to be same as: r'are|ar'
print(re.sub(r'are|ar|art', r'X', WORDS))
# phew, finally this one works as needed
print(re.sub(r'are|art|ar', r'X', WORDS))

words = ['hand', 'handy', 'handful']
alt = re.compile('|'.join(sorted(words, key=len, reverse=True)))
print(alt.pattern)
print(alt.sub(r'X', 'hands handful handed handy'))
# without sorting, alternation order will come into play
print(re.sub('|'.join(words), r'X', 'hands handful handed handy'))
