#!/usr/bin/env python
"""
######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : anchors
# @created     : Friday Feb 03, 2023 14:12:55 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import re

print(bool(re.search(r'\Acat', 'cater')))
print(bool(re.search(r'\Acat', 'concatenation')))
print(bool(re.search(r'\Ahi', 'hi hello\ntop spot')))
print(bool(re.search(r'\Atop', 'hi hello\ntop spot')))
# \Z is placed as a suffix to the pattern
print(bool(re.search(r'are\Z', 'spare')))
print(bool(re.search(r'are\Z', 'nearest')))
words = ['surrender', 'unicorn', 'newer', 'door', 'empty', 'eel', 'pest']
print([w for w in words if re.search(r'er\Z', w)])
print([w for w in words if re.search(r't\Z', w)])
# Combining both the start and end string anchors, you can restrict the matching to the whole
# string. Similar to comparing strings using the == operator.
word_pat = re.compile(r'\Acat\Z')
print(bool(word_pat.search('cat')))
print(bool(word_pat.search('cater')))
word_pat = re.compile(r'\Acat\Z')
print(bool(word_pat.search('cat')))
print(bool(word_pat.search('cater')))
print(bool(word_pat.search('concatenation')))

word_pat = re.compile(r'\Aat')
print(bool(word_pat.search('cater', 1)))
print(bool(word_pat.search('cater'[1:])))
# insert text at the start of a string
# first argument to re.sub is the search RE
# second argument is the replacement value
# third argument is the string value to be acted upon
print(re.sub(r'\A', r're', 'live'))
print(re.sub(r'\A', r're', 'send'))
# appending text
print(re.sub(r'\Z', r'er', 'cat'))
print(re.sub(r'\Z', r'er', 'hack'))
WORD = 'cater'
# this will return a string object, won't modify 'word' variable
print(re.sub(r'\Acat', r'hack', WORD))
# need to explicitly assign the result if 'word' has to be changed
word = re.sub(r'\Acat', r'hack', WORD)
print(word)

PETS = 'cat and dog'
print(bool(re.search(r'^cat', PETS)))
print(bool(re.search(r'^dog', PETS)))
print(bool(re.search(r'dog$', PETS)))
print(bool(re.search(r'^dog$', PETS)))
GREETING = 'hi there\nhave a nice day\n'
print(bool(re.search(r'day$', GREETING)))
print(bool(re.search(r'day\n$', GREETING)))
print(bool(re.search(r'day\Z', GREETING)))
print(bool(re.search(r'day\n\Z', GREETING)))

# check if any line in the string starts with 'top'
print(bool(re.search(r'^top', 'hi hello\ntop spot', flags=re.M)))
# check if any line in the string ends with 'ar'
print(bool(re.search(r'ar$', 'spare\npar\ndare', flags=re.M)))
# filter all elements having lines ending with 'are'
elements = ['spare\ntool', 'par\n', 'dare']
print([e for e in elements if re.search(r'are$', e, flags=re.M)])
print(bool(re.search(r'^par$', 'spare\npar\ndare', flags=re.M)))
IP_LINES = 'catapults\nconcatenate\ncat'
print(re.sub(r'^', r'* ', IP_LINES, flags=re.M))
print(re.sub(r'$', r'.', IP_LINES, flags=re.M))

WORDS = 'par spar apparent spare part'
# replace 'par' irrespective of where it occurs
print(re.sub(r'par', r'X', WORDS))
# replace 'par' only at start of word
print(re.sub(r'\bpar', r'X', WORDS))
# replace 'par' only at end of word
print(re.sub(r'par\b', r'X', WORDS))
# replace 'par' only if it is not part of another word
print(re.sub(r'\bpar\b', r'X', WORDS))

# space separated words to double quoted csv
# note the use of 'replace' string method
# 'translate' method can also be used
print(re.sub(r'\b', r'"', WORDS).replace(' ', ','))
print(re.sub(r'\b', r' ', '-----hello-----'))
# make a programming statement more readable
# shown for illustration purpose only, won't work for all cases
print(re.sub(r'\b', r' ', 'foo_baz=num1+35*42/num2'))
# excess space at start/end of string can be stripped off
# later you'll learn how to add a qualifier so that strip is not needed
print(re.sub(r'\b', r' ', 'foo_baz=num1+35*42/num2').strip())

# replace 'par' if it is not start of word
print(re.sub(r'\Bpar', r'X', WORDS))
# replace 'par' at end of word but not whole word 'par'
print(re.sub(r'\Bpar\b', r'X', WORDS))
# replace 'par' if it is not end of word
print(re.sub(r'par\B', r'X', WORDS))
# replace 'par' if it is surrounded by word characters
print(re.sub(r'\Bpar\B', r'X', WORDS))

print(re.sub(r'\b', r':', 'copper'))
print(re.sub(r'\B', r':', 'copper'))
print(re.sub(r'\b', r' ', '-----hello-----'))
print(re.sub(r'\B', r' ', '-----hello-----'))

# For the given input string, change only whole word red to brown
WORDS = 'bred red spread credible'
print(re.sub(r'\bred\b', r'brown', WORDS))
# For the given input list, filter all elements that contains 42
# surrounded by word characters.
words = ['hi42bye', 'nice1423', 'bad42', 'cool_42a', 'fake4b']
print([w for w in words if re.search(r'\B42\B', w)])
# For the given input list, filter all elements that start with den or end
# with ly
foo = ['lovely', '1 dentist', '2 lonely', 'eden', 'fly away', 'dent']
print([e for e in foo if re.search(r'^den', e) or re.search(r'ly$', e)])
# For the given input string, change whole word mall only if it is at
# start of line.
PARA = '''\
ball fall wall tall
mall call ball pall
wall mall ball fall'''
print(re.sub(r'^mall', r'1234', PARA, flags=re.M))
