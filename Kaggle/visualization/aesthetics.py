#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

pd.set_option("display.max_rows", 5)
pd.set_option("display.max_columns", 6)
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt

plt.rcParams.update({"figure.max_open_warning": 0})
import seaborn as sns

sns.set_theme(color_codes=True)
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages("aesthetics.pdf")
print("Setup Complete")


def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * 0.5) * (7 - i) * flip)


sinplot()
pp.savefig()
plt.clf()

sns.set_theme()
sinplot()
pp.savefig()
plt.clf()

sns.set_style("whitegrid")
data = np.random.normal(size=(20, 6)) + np.arange(6) / 2
plot = sns.boxplot(data=data)
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

f, ax = plt.subplots()
sns.violinplot(data=data)
sns.despine(offset=10, trim=True)
pp.savefig()
plt.clf()

sns.set_style("whitegrid")
sns.boxplot(data=data, palette="deep")
sns.despine(left=True)
pp.savefig()
plt.clf()

f = plt.figure(figsize=(6, 6))
gs = f.add_gridspec(2, 2)

with sns.axes_style("darkgrid"):
    ax = f.add_subplot(gs[0, 0])
    sinplot()

with sns.axes_style("white"):
    ax = f.add_subplot(gs[0, 1])
    sinplot()

with sns.axes_style("ticks"):
    ax = f.add_subplot(gs[1, 0])
    sinplot()

with sns.axes_style("whitegrid"):
    ax = f.add_subplot(gs[1, 1])
    sinplot()

f.tight_layout()

sns.axes_style()

sns.set_style("darkgrid", {"axes.facecolor": ".9"})
sinplot()

pp.savefig()
plt.clf()

sns.set_theme()
sns.set_context("paper")
sinplot()

pp.savefig()
plt.clf()

sns.set_context("talk")
sinplot()
pp.savefig()
plt.clf()

sns.set_context("poster")
sinplot()
pp.savefig()
plt.clf()

sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 2.5})
sinplot()
pp.savefig()
plt.clf()

pp.close()
