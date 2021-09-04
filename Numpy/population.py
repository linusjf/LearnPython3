#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

data = np.loadtxt('population.txt')
print(data)
np.savetxt('pop2.txt', data)
data2 = np.loadtxt('pop2.txt')
print(data2)
