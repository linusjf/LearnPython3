#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This is always assumed but is included here as an introduction.
import pandas as pd 
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
# The PDF document
pdf_pages = PdfPages("helloworld.pdf")
np.random.seed(0)
# array of normally distributed random numbers
values = np.random.randn(100) 
# generate a pandas series
s = pd.Series(values) 
# hist computes distribution
s.plot(kind='hist', title='Normally distributed random values') 
pdf_pages.savefig()
pdf_pages.close()
print(s.describe())
df = pd.DataFrame({'A': [1, 2, 1, 4, 3, 5, 2, 3, 4, 1],
 'B': [12, 14, 11, 16, 18, 18, 22, 13, 21, 17],
 'C': ['a', 'a', 'b', 'a', 'b', 'c', 'b', 'a', 'b', 'a']})
print(df.describe())
print(df['C'].describe())
