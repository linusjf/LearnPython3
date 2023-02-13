#!/usr/bin/env python
"""
######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : characters
# @created     : Monday Feb 13, 2023 13:18:03 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import re

words = ['cute', 'cat', 'cot', 'coat', 'cost', 'scuttle']
print([w for w in words if re.search(r'c[ou]t', w)])
# same as: r'(a|e|o)+t'
print(re.sub(r'[aeo]+t', r'X', 'meeting cute boat site foot'))
# all digits
print(re.findall(r'[0-9]+', 'Sample123string42with777numbers'))
# whole words made up of lowercase alphabets and digits only
print(re.findall(r'\b[a-z0-9]+\b', 'coat Bin food tar12 best'))
# whole words made up of lowercase alphabets, but starting with 'p' to 'z'
print(re.findall(r'\b[p-z][a-z]*\b', 'coat tin food put stoop best'))
# whole words made up of only 'a' to 'f' and 'p' to 't' lowercase alphabets
print(re.findall(r'\b[a-fp-t]+\b', 'coat tin food put stoop best'))
