#!/usr/bin/env python3
""" Regex expressions """
import re
XX = "guru99,education is fun"
R1 = re.findall(r"^\w+", XX)
print(R1)
print((re.split(r'\s', 'we are splitting the words')))
print((re.split(r's', 'split the words')))
