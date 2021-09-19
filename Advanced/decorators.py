#!/usr/bin/env python

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : decorators
# @created     : Sunday Sep 19, 2021 16:36:31 IST
# @description : 
# -*- coding: utf-8 -*-'
######################################################################

import time
from functools import wraps
def timer(func):
    @wraps(func)
    def wrapper(a,b):
        print(f"{func.__name__!r} begins")
        start_time = time.time()
        result = func(a,b)
        print(f"{func.__name__!r} ends in {time.time()-start_time} secs")
        return result
    return wrapper

@timer
def somefunc(a,b):
    output = a+b
    return output

a = somefunc(4,5)
