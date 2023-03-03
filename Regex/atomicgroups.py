#!/usr/bin/env python
"""
Atomicgroups.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : atomicgroups
# @created     : Friday Mar 03, 2023 14:15:17 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import re

atomic = re.compile(r"(?>A|.B)C")
print(bool(atomic.search("ABC")))

atomic = re.compile("(?>A+)[A-Z]C")
print(bool(atomic.search("AAC")))
possessive = re.compile("A++[A-Z]C")
print(bool(possessive.search("AAC")))
