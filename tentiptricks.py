#!/usr/bin/env python3
"""Ten Tip Tricks"""
import os
import socket
import sys
from collections import Counter

# 1. In-Place Swapping Of Two Numbers.
X, y = 10, 20

print(X, y)

X, y = y, X

print(X, y)

# 2. Reversing a string in Python

_a = "GeeksForGeeks"

print("Reverse is", _a[::-1])

# 3. Create a single string from all the elements in list

_a = ["Geeks", "For", "Geeks"]

print(" ".join(_a))

# 4. Chaining Of Comparison Operators.

_n = 10

result = 1 < _n < 20

print(result)

result = 1 > _n <= 9

print(result)

# 4. Print The File Path Of Imported Modules.

print(os)

print(socket)

# 5. Use Of Enums In Python.

class MyName:
    """Enum definition"""
    Geeks, For, Geeks = range(3)

print(MyName.Geeks)
print(MyName.For)
print(MyName.Geeks)

# 6. Return Multiple Values From Functions.

def x():
    """return multiple values"""
    return 1, 2, 3, 4

a, b, c, d = x()

print(a, b, c, d)

# 7. Find The Most Frequent Value In A List.

test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]

print(max(set(test), key=test.count))

# 8. Check The Memory Usage Of An Object.

X = 1

print(sys.getsizeof(X))

# 9. Print string N times.

n = 2

a = "GeeksforGeeks"

print(a * n) 

# 10. Checking if two words are anagrams

def is_anagram(str1, str2): 
    """check if anagram"""
    return Counter(str1) == Counter(str2) 

print(is_anagram('geek', 'eegk'))

print(is_anagram('geek', 'peek'))     
