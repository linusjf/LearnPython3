#!/usr/bin/env python
"""
######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : backreferences
# @created     : Tuesday Feb 14, 2023 15:56:54 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import re

# remove square brackets that surround digit characters
print(re.sub(r'\[(\d+)\]', r'\1', '[52] apples and [31] mangoes'))
# replace __ with _ and delete _ if it is alone
print(re.sub(r'(_)?_', r'\1', '_foo_ __123__ _baz_'))
# add something around the matched strings
print(re.sub(r'\d+', r'(\g<0>0)', '52 apples and 31 mangoes'))
# note the use of count flag
# otherwise empty string matching with * will come into play
print(re.sub(r'.*', r'Hi,\g<0>. Have a nice day!', 'Linus Fernandes', count=1))
# swap words that are separated by a comma
print(re.sub(r'(\w+),(\w+)', r'\2,\1', 'good,bad 42,24'))

# whole words that have at least one consecutive repeated character
words = ['effort', 'flee', 'facade', 'oddball', 'rat', 'tool']
print([w for w in words if re.search(r'\b\w*(\w)\1\w*\b', w)])
# remove any number of consecutive duplicate words separated by space
# quantifiers can be applied to backreferences too!
print(re.sub(r'\b(\w+)( \1)+\b', r'\1', 'aa a a a 42 f_1 f_1 f_13.14'))

# without capture group
print(re.split(r'\d+', 'Sample123string42with777numbers'))
# to include the matching delimiter strings as well in the output
print(re.split(r'(\d+)', 'Sample123string42with777numbers'))
# optional argument maxsplit can be used to specify no. of splits
# setting to 1 gives behavior like partition string method
print(re.split(r'(1*2)', '3111111111125111142', maxsplit=1))
# normal capture group will hinder ability to get whole match
# non-capturing group to the rescue
print(re.findall(r'\b\w*(?:st|in)\b', 'cost akin more east run against'))
# capturing wasn't needed here, only common grouping and quantifier
print(re.split(r'hand(?:y|ful)?', '123hand42handy777handful500'))
# with normal grouping, need to keep track of all the groups
print(re.sub(r'\A(([^,]+,){3})([^,]+)', r'\1(\3)', '1,2,3,4,5,6,7', count=1))
# using non-capturing groups, only relevant groups have to be tracked
print(re.sub(r'\A((?:[^,]+,){3})([^,]+)', r'\1(\2)', '1,2,3,4,5,6,7', count=1))
WORDS = 'effort flee facade oddball rat tool'
# whole words containing at least one consecutive repeated character
repeat_char = re.compile(r'\b\w*(\w)\1\w*\b')
# () in findall will only return text matched by capture groups
print(repeat_char.findall(WORDS))

WORDS = 'effort flee facade oddball rat tool'
# whole words containing at least one consecutive repeated character
repeat_char = re.compile(r'\b\w*(\w)\1\w*\b')
# () in findall will only return text matched by capture groups
print(repeat_char.findall(WORDS))
m_iter = repeat_char.finditer(WORDS)
print([m[0] for m in m_iter])

# giving names to first and second captured words
re.sub(r'(?P<fw>\w+),(?P<sw>\w+)', r'\g<sw>,\g<fw>', 'good,bad 42,24')
SENTENCE = 'I bought an apple'
m = re.search(r'(?P<fruit>\w+)\Z', SENTENCE)
print(m[1])
print(m['fruit'])
print(m.group('fruit'))
