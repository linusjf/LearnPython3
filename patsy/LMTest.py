#!/usr/bin/env python
# -*- coding: utf-8 -*-

from patsy import demo_data
from LM import LM
import numpy as np

data = demo_data("x", "y", "a")
print(data["x"])
# Old and boring approach (but it still works):
X = np.column_stack(([1] * len(data["y"]), data["x"]))
print(X)
print(LM((data["y"], X)))
m = LM("y ~ x", data)
print(m)
print(m.loglik(data))
print(m.loglik({"x": [10, 20, 30], "y": [-1, -2, -3]}))
# Your users get support for categorical predictors for free:
print(LM("y ~ a", data))
print(LM("y ~ np.log(x ** 2)", data))
