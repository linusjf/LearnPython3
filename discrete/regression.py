#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('regression.pdf')
print("Setup Complete")
# Importing the csv file
df = pd.read_csv("auto-mpg.csv")
# Plotting the pairplot
sns.pairplot(df, diag_kind="kde")
pp.savefig()
pp.close()
