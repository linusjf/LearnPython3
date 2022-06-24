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
