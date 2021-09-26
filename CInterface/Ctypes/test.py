#!/usr/bin/env python

import ctypes
import cos_module
print(dir(cos_module))
print(cos_module.cos_func(1.0))
print(cos_module.cos_func(0.0))
print(cos_module.cos_func(3.14159265359))
try:
    cos_module.cos_func('foo')
except ctypes.ArgumentError as ae:
    print(f"'foo' {ae}")

