#!/usr/bin/env python3
""" Regex expressions """
import re
XX = "guru99,education is fun"
R1 = re.findall(r"^\w+", XX)
print(R1)
print((re.split(r'\s', 'we are splitting the words')))
print((re.split(r's', 'split the words')))
words = ["guru99 get", "guru99 give", "guru Selenium"]

for element in words:
    z = re.match("(g\w+)\W(g\w+)", element)
    if z:
        print((z.groups()))

for element in words:
    z = re.match("(g\w+)\W(S\w+)", element)
    if z:
        print((z.groups()))
