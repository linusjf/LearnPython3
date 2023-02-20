#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup, Extension
from Cython.Distutils import build_ext

exts = [Extension("cos_module", ["cos_module.pyx"])]

for e in exts:
    e.cython_directives = {"language_level": "3"}  # all are Python-3

setup(cmdclass={"build_ext": build_ext}, ext_modules=exts)
