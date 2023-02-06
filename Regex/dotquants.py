#!/usr/bin/env python
"""
######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : dotquants
# @created     : Monday Feb 06, 2023 16:05:00 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import re

# matches character 'c', any character and then character 't'
print(re.sub(r'c.t', r'X', 'tac tin cat abc;tuv acute'))
# matches character 'r', any two characters and then character 'd'
print(re.sub(r'r..d', r'X', 'breadth markedly reported overrides'))
# matches character '2', any character and then character '3'
print(re.sub(r'2.3', r'8', '42\t35'))
