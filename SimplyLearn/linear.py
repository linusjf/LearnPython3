#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import libraries
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# The PDF document
pdf_pages = PdfPages("linear.pdf")

companies = pd.read_csv("1000_companies.csv")
X = companies.iloc[:, :-1].values
Y = companies.iloc[:, :4].values

print(companies.head())

ax = sns.heatmap(companies.corr())
pdf_pages.savefig(bbox_inches='tight')

pdf_pages.close()
