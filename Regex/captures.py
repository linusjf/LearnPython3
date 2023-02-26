#!/usr/bin/env python
"""
Captures.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : captures
# @created     : Sunday Feb 26, 2023 05:31:58 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import regex

regexx = regex.compile(r"([A-Z])_(?1)")
SOURCE = "AA_BB"
print(regexx.findall(SOURCE))
regexx = regex.compile(r"(([A-Z])\2)_(?1)")
print(regexx.findall(SOURCE))
