#!/usr/bin/env python
"""
Match.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : match
# @created     : Monday Feb 13, 2023 09:35:11 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import re

print(re.search(r"ab*c", "abc ac adc abbbc"))
print(re.search(r"b.*d", "abc ac adc abbbc"))
print(re.search(r"b.*d", "abc ac adc abbbc"))
# retrieving entire matched portion)
print(re.search(r"b.*d", "abc ac adc abbbc")[0])
# can also pass an index by calling 'group' method on the Match object)
print(re.search(r"b.*d", "abc ac adc abbbc").group(0))
# capture group example)
m = re.search(r"a(.*)d(.*a)", "abc ac adc abbbc")
# to get matched portion of second capture group)
print(m[2])
# to get a tuple of all the capture groups)
print(m.groups())
# m[0] will contain entire matched portion)
# a^2 and b^2 for the two matches in this example)
print(re.sub(r"(a|b)\^2", lambda m: m[0].upper(), "a^2 + b^2 - C*3"))

print(re.findall(r"ab*c", "abc ac adc abbbc"))
print(re.findall(r"ab+c", "abc ac adc abbbc"))
print(re.findall(r"\bs?pare?\b", "par spar apparent spare part pare"))
print(re.findall(r"t.*a", "that is quite a fabricated tale"))
print(re.findall(r"t.*?a", "that is quite a fabricated tale"))
print(re.findall(r"a(b*)c", "abc ac adc abbc xabbbcz bbb bc abbbbbc"))
print(re.findall(r"(x*):(y*)", "xx:yyy x: x:yy :y"))
print(re.finditer(r"ab+c", "abc ac adc abbbc"))
m_iter = re.finditer(r"ab+c", "abc ac adc abbbc")
for m in m_iter:
    print(m)
# same as: re.findall(r'(x*):(y*)', 'xx:yyy x: x:yy :y')
m_iter = re.finditer(r"(x*):(y*)", "xx:yyy x: x:yy :y")
print([(m[1], m[2]) for m in m_iter])
# work with entire matched portions
m_iter = re.finditer(r"ab+c", "abc ac adc abbbc")
for m in m_iter:
    print(m[0].upper())
# to get start and end+1 index of entire matched portion
# pass a number as argument to get span of that particular capture group
m_iter = re.finditer(r"ab+c", "abc ac adc abbbc")
for m in m_iter:
    print(m.span())

print("\n---------------")
print("Exercises")
print("---------------\n")

# a) For the given strings, extract the matching portion from first is to
# last t
STR1 = "What is the biggest fruit you have seen?"
STR2 = "Your mission is to read and practice consistently"
expr = re.compile(r"is.*t")  # add your solution here
print(re.findall(expr, STR1)[0])  # add your solution here
print(re.findall(expr, STR2)[0])  # add your solution here

# Transform the given input strings to the expected output as shown below.
ROW1 = "-2,5 4,+3 +42,-53 "
ROW2 = "1.32,-3.14 634,5.63 "
EXPR = r"(\-?\+?\d+\.?\d*),(\-?\+?\d+\.?\d*)"
m_iter = re.finditer(EXPR, ROW1)
print([(int(m[1]) + int(m[2])) for m in m_iter])
m_iter = re.finditer(EXPR, ROW2)
print([(float(m[1]) + float(m[2])) for m in m_iter])
