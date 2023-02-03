#!/usr/bin/env python
"""
######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : examples
# @created     : Friday Feb 03, 2023 13:19:59 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import re

FILENAME = 'programming_quotes.txt'
word = re.compile("two")  ##### add your solution here
with open(FILENAME, 'r', encoding="utf-8") as ip_file:
    for ip_line in ip_file:
        if word.search(ip_line):
            print(ip_line, end='')

PURCHASES = '''\
... apple 24
... mango 50
... guava 42
... onion 31
... water 10'''
num = re.compile("2")  ##### add your solution here
for line in PURCHASES.split('\n'):
    if not num.search(line):
        print(line)
