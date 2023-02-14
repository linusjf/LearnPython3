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
