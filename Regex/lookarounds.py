#!/usr/bin/env python
"""
######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : lookarounds
# @created     : Wednesday Feb 15, 2023 11:20:05 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import re

# change 'foo' only if it is not followed by a digit character
# note that end of string satisfies the given assertion
# 'foofoo' has two matches as the assertion doesn't consume characters
print(re.sub(r'foo(?!\d)', r'baz', 'hey food! foo42 foot5 foofoo'))
# change 'foo' only if it is not preceded by _
# note how 'foo' at start of string is matched as well
print(re.sub(r'(?<!_)foo', r'baz', 'foo _foo 42foofoo'))
# overlap example
# the final _ was replaced as well as played a part in the assertion
print(re.sub(r'(?<!_)foo.', r'baz', 'food _fool 42foo_foot'))

# change whole word only if it is not preceded by : or -
print(re.sub(r'(?<![:-])\b\w+\b', r'X', ':cart <apple -rest ;tea'))
# add space to word boundaries, but not at start or end of string
# similar to: re.sub(r'\b', r' ', 'foo_baz=num1+35*42/num2').strip()
print(re.sub(r'(?<!\A)\b(?!\Z)', r' ', 'foo_baz=num1+35*42/num2'))

# extract digits only if it is followed by ,
# note that end of string doesn't qualify as this is positive assertion
print(re.findall(r'\d+(?=,)', '42 foo-5, baz3; x-83, y-20: f12'))
# extract digits only if it is preceded by - and followed by ; or :
print(re.findall(r'(?<=-)\d+(?=[:;])', '42 foo-5, baz3; x-83, y-20: f12'))
# except first and last fields
print(re.findall(r'(?<=,)[^,]+(?=,)', '1,two,3,four,5'))
# replace empty fields with NA
# note that in this case, order of lookbehind and lookahead doesn't matter
print(re.sub(r'(?<![^,])(?![^,])', r'NA', ',1,,,two,3,,,'))
print(re.sub(r'(\S+\s+)(?=(\S+)\s)', r'\1\2\n', 'a b c d e'))
# and of course, use non-capturing group where needed
print(re.findall(r'(?<=(po|ca)re)\d+', 'pore42 car3 pare7 care5'))
print(re.findall(r'(?<=(?:po|ca)re)\d+', 'pore42 car3 pare7 care5'))

words = ['sequoia', 'subtle', 'questionable', 'exhibit', 'equation']
# words containing 'b' and 'e' and 't' in any order
# same as: r'b.*e.*t|b.*t.*e|e.*b.*t|e.*t.*b|t.*b.*e|t.*e.*b'
print([w for w in words if re.search(r'(?=.*b)(?=.*e).*t', w)])
# words containing all lowercase vowels in any order
print([w for w in words if re.search(r'(?=.*a)(?=.*e)(?=.*i)(?=.*o).*u', w)])

# allowed
print(re.findall(r'(?<=(?:po|ca)re)\d+', 'pore42 car3 pare7 care5'))
print(re.findall(r'(?<=\b[a-z]{4})\d+', 'pore42 car3 pare7 care5'))
# not allowed
try:
    re.findall(r'(?<!car|pare)\d+', 'pore42 car3 pare7 care5')
except re.error as e:
    print(e)
try:
    re.findall(r'(?<=\b[a-z]+)\d+', 'pore42 car3 pare7 care5')
except re.error as e:
    print(e)
try:
    re.sub(r'(?<=\A|,)(?=,|\Z)', r'NA', ',1,,,two,3,,,')
except re.error as e:
    print(e)
