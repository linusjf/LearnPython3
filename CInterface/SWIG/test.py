#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cos_module

dir(cos_module)
print(cos_module.cos_func(1.0))
print(cos_module.cos_func(0.0))
print(cos_module.cos_func(3.14159265359))
try:
    print(cos_module.cos_func("foo"))
except TypeError as te:
    print(f"'foo' {te}")
