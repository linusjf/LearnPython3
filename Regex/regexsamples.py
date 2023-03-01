#!/usr/bin/env python
"""
Regexsamples.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : regexsamples
# @created     : Wednesday Mar 01, 2023 23:19:54 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
from time import sleep
import regex


def fast_replace(_):
    """Fast replace."""
    return "X"


def slow_replace(_):
    """Slow replace."""
    sleep(0.5)
    return "X"


print(regex.sub(r"[a-z]", fast_replace, "abcde", timeout=2))
print(regex.sub(r"[a-z]", slow_replace, "abcde", timeout=2))

m = regex.match(r"(?|(first)|(second))", "first")
if m:
    print(m.groups())
m = regex.match(r"(?|(first)|(second))", "second")
if m:
    print(m.groups())

print(regex.findall(r".", "abc"))
print(regex.findall(r"(?r).", "abc"))
print(regex.findall(r"..", "abcde"))
print(regex.findall(r"(?r)..", "abcde"))
