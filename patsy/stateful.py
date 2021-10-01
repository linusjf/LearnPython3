#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import patsy
from patsy import dmatrix, build_design_matrices, incr_dbuilder
data = {"x": [1, 2, 3, 4]}
new_data = {"x": [5, 6, 7, 8]}
fixed_mat = dmatrix("center(x)", data)
print(fixed_mat)
d = build_design_matrices([fixed_mat.design_info], new_data)[0]
print(d)

data_chunked = [{"x": data["x"][:2]},
                {"x": data["x"][2:]}]
dinfo = incr_dbuilder("center(x)", lambda: iter(data_chunked))

# Correct!
d = np.row_stack([build_design_matrices([dinfo], chunk)[0] for chunk in data_chunked])
print(d)
d = build_design_matrices([dinfo], new_data)[0]
print(d)

class MyExampleCenter(object):
    def __init__(self):
        self._total = 0
        self._count = 0
        self._mean = None

    def memorize_chunk(self, x):
        self._total += np.sum(x)
        self._count += len(x)

    def memorize_finish(self):
        self._mean = self._total * 1. / self._count

    def transform(self, x):
        return x - self._mean

my_example_center = patsy.stateful_transform(MyExampleCenter)
print(my_example_center(np.array([1, 2, 3])))
