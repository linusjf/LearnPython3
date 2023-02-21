#!/usr/bin/env python
"""Regex samples."""
# -*- coding: utf-8 -*-
import re
import regex

SENTENCE = "This is a sample string"
# check if 'SENTENCE' contains the given string argument
print("is" in SENTENCE)
print("xyz" in SENTENCE)
# need to load the re module before use
# check if 'SENTENCE' contains the pattern described by RE argument
print(bool(re.search(r"is", SENTENCE)))
print(bool(re.search(r"xyz", SENTENCE)))

if re.search(r"ring", SENTENCE):
    print("mission success")
if not re.search(r"xyz", SENTENCE):
    print("mission failed")
words = ["cat", "attempt", "tattle"]
print([w for w in words if re.search(r"tt", w)])
print(all(re.search(r"at", w) for w in words))
print(any(re.search(r"stat", w) for w in words))

pet = re.compile(r"dog")
print(type(pet))
print(bool(pet.search("They bought a dog")))
print(bool(pet.search("A cat crossed their path")))

word = re.compile(r"is")
print(bool(word.search(SENTENCE, 4)))
print(bool(word.search(SENTENCE, 6)))
# search for 'is' between 3rd and 4th characters
bool(word.search(SENTENCE, 2, 4))

BYTE_DATA = b"This is a sample string"
# error message truncated for presentation purposes
try:
    print(re.search(rb"is", BYTE_DATA))
except TypeError as te:
    print(te)
print(bool(re.search(rb"is", BYTE_DATA)))
print(bool(re.search(rb"xyz", BYTE_DATA)))

print(bool(regex.search(r"is", SENTENCE)))
print(bool(regex.search(r"xyz", SENTENCE)))
