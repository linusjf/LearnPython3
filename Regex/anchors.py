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
