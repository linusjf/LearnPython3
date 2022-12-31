#!/usr/bin/env python
# -*- coding: utf-8 -*-
sentence = 'This is a sample string'
# check if 'sentence' contains the given string argument
print('is' in sentence)
print('xyz' in sentence)
# need to load the re module before use
import re
# check if 'sentence' contains the pattern described by RE argument
print(bool(re.search(r'is', sentence)))
print(bool(re.search(r'xyz', sentence)))
