#!/usr/bin/env python
# -*- coding: utf-8 -*-

from patsy import ModelDesc
print(ModelDesc.from_formula("y ~ x").describe())
print(ModelDesc.from_formula("y ~ x + x + x").describe())
print(ModelDesc.from_formula("y ~ -1 + x").describe())
print(ModelDesc.from_formula("~ -1").describe())
print(ModelDesc.from_formula("y ~ a:b").describe())
print(ModelDesc.from_formula("y ~ a*b").describe())
print(ModelDesc.from_formula("y ~ (a + b + c + d) ** 2").describe())
print(ModelDesc.from_formula("y ~ (a + b)/(c + d)").describe())
print(ModelDesc.from_formula("np.log(x1 + x2) "
                       "+ (x + {6: x3, 8 + 1: x4}[3 * i])").describe())
#Sometimes it might be easier to read if you put the processed formula back into formula notation using ModelDesc.describe():

desc = ModelDesc.from_formula("y ~ (a + b + c + d) ** 2")
print(desc.describe())
