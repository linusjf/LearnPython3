""" Example of wrapping cos function from math.h using Cython. """

#cdef extern from "math.h":
 #   double cos(double arg)

#def cos_func(arg):
 #   return cos(arg)

""" Simpler example of wrapping cos function from math.h using Cython. """

from libc.math cimport cos

def cos_func(arg):
    return cos(arg)
