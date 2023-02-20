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

sns.set_theme(style="whitegrid")
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages("stripplots.pdf")
print("Setup Complete")

tips = sns.load_dataset("tips")
print(tips.head())
ax = sns.stripplot(x=tips["total_bill"])
pp.savefig()
ax.figure.clear()

ax = sns.stripplot(x="day", y="total_bill", data=tips)
pp.savefig()
ax.figure.clear()

ax = sns.stripplot(x="day", y="total_bill", data=tips, jitter=0.05)
pp.savefig()
ax.figure.clear()

ax = sns.stripplot(x="day", y="total_bill", data=tips, jitter=0.05)
pp.savefig()
ax.figure.clear()

ax = sns.stripplot(x="total_bill", y="day", data=tips, linewidth=1)
pp.savefig()
ax.figure.clear()

ax = sns.stripplot(x="sex", y="total_bill", hue="day", data=tips)
pp.savefig()
ax.figure.clear()

ax = sns.stripplot(x="day", y="total_bill", hue="smoker", data=tips, palette="Set2", dodge=True)
pp.savefig()
ax.figure.clear()

ax = sns.stripplot(x="time", y="tip", data=tips, order=["Dinner", "Lunch"])
pp.savefig()
ax.figure.clear()

ax = sns.stripplot(
    x="day",
    y="total_bill",
    hue="smoker",
    data=tips,
    palette="Set2",
    size=20,
    marker="D",
    edgecolor="gray",
    alpha=0.25,
)
pp.savefig()
ax.figure.clear()

import numpy as np

ax = sns.boxplot(x="tip", y="day", data=tips, whis=np.inf)
ax = sns.stripplot(x="tip", y="day", data=tips, color=".3")
pp.savefig()
ax.figure.clear()

ax = sns.violinplot(x="day", y="total_bill", data=tips, inner=None, color=".8")
ax = sns.stripplot(x="day", y="total_bill", data=tips)
pp.savefig()
ax.figure.clear()

g = sns.catplot(
    x="sex",
    y="total_bill",
    hue="smoker",
    col="time",
    data=tips,
    kind="strip",
    height=4,
    aspect=0.7,
)
pp.savefig()
g.figure.clear()

pp.close()
