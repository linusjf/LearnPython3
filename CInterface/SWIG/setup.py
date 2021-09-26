#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup, Extension

setup(ext_modules=[Extension("_cos_module",
      sources=["cos_module.c", "cos_module.i"])])
