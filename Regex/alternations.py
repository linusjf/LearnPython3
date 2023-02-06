#!/usr/bin/env python
"""
######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : alternations
# @created     : Sunday Feb 05, 2023 20:08:41 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import re

# match either 'cat' or 'dog'
print(bool(re.search(r'cat|dog', 'I like cats')))
print(bool(re.search(r'cat|dog', 'I like dogs')))
print(bool(re.search(r'cat|dog', 'I like parrots')))
# replace either 'cat' at start of string or 'cat' at end of word
print(re.sub(r'\Acat|cat\b', r'X', 'catapults concatenate cat scat'))
# replace either 'cat' or 'dog' or 'fox' with 'mammal'
print(re.sub(r'cat|dog|fox', r'mammal', 'cat dog bee parrot fox'))
# The join string method can be used to build the alternation list automatically
# from an iterable of strings.
print('|'.join(['car', 'jeep']))
words = ['cat', 'dog', 'fox']
print('|'.join(words))
print(re.sub('|'.join(words), r'mammal', 'cat dog bee parrot fox'))
# without grouping
print(re.sub(r'reform|rest', r'X', 'red reform read arrest'))
# with grouping
print(re.sub(r're(form|st)', r'X', 'red reform read arrest'))
# without grouping
print(re.sub(r'\bpar\b|\bpart\b', r'X', 'par spare part party'))
print(re.sub(r'\b(par|part)\b', r'X', 'par spare part party'))
# taking out common characters as well
# you'll later learn a better technique instead of using empty alternate
print(re.sub(r'\bpar(|t)\b', r'X', 'par spare part party'))

words = ['cat', 'par']
print('|'.join(words))
# without word boundaries, any matching portion will be replaced
print(re.sub('|'.join(words), r'X', 'cater cat concatenate par spare'))
# note how raw string is used on either side of concatenation
# avoid f-strings unless you know how to compensate for RE
alt = re.compile(r'\b(' + '|'.join(words) + r')\b')
# only whole words will be replaced now
alt.sub(r'X', 'cater cat concatenate par spare')
# this is how the above RE looks as a normal string
print(alt.pattern)
print(alt.pattern == r'\b(cat|par)\b')

#For the given input list, filter all elements that start with den or end with ly
foo = ['lovely', '1 dentist', '2 lonely', 'eden', 'fly away', 'dent']
se = re.compile(r'(\Aden)|(ly\Z)')
print([e for e in foo if se.search(e)])
#['lovely', '2 lonely', 'dent']
