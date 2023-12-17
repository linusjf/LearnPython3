#!/usr/bin/env python
"""
Arraypy.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : arraypy
# @created     : Sunday Dec 17, 2023 18:34:37 IST
# @description :
https://www.linkedin.com/feed/update/urn:li:activity:7142143531447492608
# -*- coding: utf-8 -*-'
######################################################################
"""
import array
import random
import sys
import time
import numpy as np

rlst = [random.randint(0, 100) for _ in range(10**7)]
rray = array.array('i', rlst)
nparray = np.array(rlst, dtype=np.int64)
print("Object size comparison")
print(f"Size: {sys.getsizeof(rlst):>15,} bytes | "
      f"{rray.buffer_info()[1] * rray.itemsize:>15,} bytes | "
      f"{nparray.size * nparray.itemsize:>15,} bytes | ")

print("Native summation")
start = time.time()
sum(rlst)
end = time.time()
list_time = (end - start)
start = time.time()
sum(rray)
end = time.time()
array_time = (end - start)
print(f"Time: {list_time:>15.3f} sec | {array_time:>15.3f} sec")

print("Numpy summation")
start = time.time()
np.sum(rlst)
end = time.time()
list_time = (end - start)
start = time.time()
np.sum(rray)
end = time.time()
array_time = (end - start)
print(f"Time: {list_time:>15.3f} sec | {array_time:>15.3f} sec")

print("Numpy array summation")
start = time.time()
np.sum(rlst)
end = time.time()
list_time = (end - start)
start = time.time()
np.sum(nparray)
end = time.time()
array_time = (end - start)
print(f"Time: {list_time:>15.3f} sec | {array_time:>15.3f} sec")
