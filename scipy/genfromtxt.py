#!/usr/bin/env python
# -*- coding: utf-8 -*-

from io import StringIO
import numpy as np

s = StringIO("1,1.3,abcde")
data = np.genfromtxt(
    s, dtype=[("myint", "i8"), ("myfloat", "f8"), ("mystring", "S5")], delimiter=","
)
print(data)

_ = s.seek(0)  # needed for StringIO example only
data = np.genfromtxt(s, dtype=None, names=["myint", "myfloat", "mystring"], delimiter=",")
print(data)
_ = s.seek(0)
data = np.genfromtxt(s, dtype="i8,f8,S5", names=["myint", "myfloat", "mystring"], delimiter=",")
print(data)
s = StringIO("11.3abcde")
data = np.genfromtxt(s, dtype=None, names=["intvar", "fltvar", "strvar"], delimiter=[1, 3, 5])
print(data)
f = StringIO(
    """
text,# of chars
hello world,11
numpy,5"""
)
print(np.genfromtxt(f, dtype="S12,S12", delimiter=","))
