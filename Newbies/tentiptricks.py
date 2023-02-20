#!/usr/bin/env python3
"""Ten Tip Tricks."""
import os
import socket
import sys
from collections import Counter

# 1. In-Place Swapping Of Two Numbers.
X, Y = 10, 20

print(X, Y)

X, Y = Y, X

print(X, Y)

# 2. Reversing a string in Python

A = "GeeksForGeeks"

print("Reverse is", A[::-1])

# 3. Create a single string from all the elements in list

A = ["Geeks", "For", "Geeks"]

print(" ".join(A))

# 4. Chaining Of Comparison Operators.

N = 10

RESULT = 1 < N < 20

print(RESULT)

RESULT = 1 > N <= 9

print(RESULT)

# 4. Print The File Path Of Imported Modules.

print(os)

print(socket)

# 5. Use Of Enums In Python.

# pylint: disable=too-few-public-methods


class MyName:
    """Enum definition."""

    Geek, For, Geeks = range(3)


# pylint: enable=too-few-public-methods


print(MyName.Geek)
print(MyName.For)
print(MyName.Geeks)

# 6. Return Multiple Values From Functions.


def multiplicity():
    """Return multiple values."""
    return 1, 2, 3, 4


A, B, C, D = multiplicity()

print(A, B, C, D)

# 7. Find The Most Frequent Value In A List.

TEST = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]

print(max(set(TEST), key=TEST.count))

# 8. Check The Memory Usage Of An Object.

X = 1

print(sys.getsizeof(X))

# 9. Print string N times.

N = 2

A = "GeeksforGeeks"

print(A * N)

# 10. Checking if two words are anagrams


def is_anagram(str1, str2):
    """Check if anagram."""
    return Counter(str1) == Counter(str2)


print(is_anagram("geek", "eegk"))

print(is_anagram("geek", "peek"))
