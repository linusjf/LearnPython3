#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
from patsy import dmatrices
df = pd.read_spss('hsb2.sav')
print(df.tail())
cols = ['ID', 'FEMALE', 'RACE', 'READ', 'WRITE']
df = pd.read_spss('hsb2.sav', usecols=cols)
print(df.head())
