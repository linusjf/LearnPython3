#!/usr/bin/env python3
""" Regex expressions """
import re
XX = "guru99,education is fun"
R1 = re.findall(r"^\w+", XX)
print(R1)
print((re.split(r'\s', 'we are splitting the words')))
print((re.split(r's', 'split the words')))
WORDS = ["guru99 get", "guru99 give", "guru Selenium"]

for element in WORDS:
    z = re.match(r"(g\w+)\W(g\w+)", element)
    if z:
        print((z.groups()))

for element in WORDS:
    z = re.match(r"(g\w+)\W(S\w+)", element)
    if z:
        print((z.groups()))

PATTERNS = ['software testing', 'guru99']
TEXT = 'software testing is fun?'
for pattern in PATTERNS:
    print('Looking for "%s" in "%s" ->' % (pattern, TEXT), end=' ')
    if re.search(pattern, TEXT):
        print('found a match!')
    else:
        print('no match')

ABC = """guru99@google.com,
careerguru99@hotmail.com,
users@yahoomail.com"""
EMAILS = re.findall(r'[\w\.-]+@[\w\.-]+', ABC)
for email in EMAILS:
    print(email)
