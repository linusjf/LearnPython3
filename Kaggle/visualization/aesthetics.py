#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
pd.set_option("display.max_rows", 5)
pd.set_option("display.max_columns", 6)
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.max_open_warning': 0})
import seaborn as sns
sns.set_theme(color_codes=True)
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('aesthetics.pdf')
print("Setup Complete")

def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)

sinplot()
pp.savefig()
plt.clf()

sns.set_theme()
sinplot()
pp.savefig()
plt.clf()

sns.set_style("whitegrid")
data = np.random.normal(size=(20, 6)) + np.arange(6) / 2
plot = sns.boxplot(data=data);
pp.savefig()
plot.figure.clear()

sns.set_style("dark")
sinplot()
pp.savefig()
plt.clf()

sns.set_style("white")
sinplot()
pp.savefig()
plt.clf()

sns.set_style("ticks")
sinplot()
pp.savefig()
plt.clf()

sinplot()
sns.despine()
pp.savefig()
plt.clf()

pp.close()
