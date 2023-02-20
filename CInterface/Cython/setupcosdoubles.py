#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup, Extension
import numpy
from Cython.Distutils import build_ext


exts = [
    Extension(
        "cos_doubles",
        sources=["_cos_doubles.pyx", "cos_doubles.c"],
        include_dirs=[numpy.get_include()],
    )
]

for e in exts:
    e.cython_directives = {"language_level": "3"}  # all are Python-3

setup(cmdclass={"build_ext": build_ext}, ext_modules=exts)
