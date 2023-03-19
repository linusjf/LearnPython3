#!/usr/bin/env python
"""
Select.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : select
# @created     : Sunday Mar 19, 2023 14:25:33 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import numpy as np

x = np.arange(6)
condlist = [x < 3, x > 3]
choicelist = [x, x**2]
print(np.select(condlist, choicelist, 42))
condlist = [x <= 4, x > 3]
choicelist = [x, x**2]
print(np.select(condlist, choicelist, 55))
