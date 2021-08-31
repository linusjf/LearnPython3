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
pp = PdfPages('boxenplots.pdf')
print("Setup Complete")

tips = sns.load_dataset("tips")
print(tips.head())
ax = sns.boxenplot(x=tips["total_bill"])
pp.savefig()
ax.figure.clear()

ax = sns.boxenplot(x="day", y="total_bill", data=tips)
pp.savefig()
ax.figure.clear()

ax = sns.boxenplot(x="day", y="total_bill", hue="smoker",
                   data=tips, palette="Set3")
pp.savefig()
ax.figure.clear()

ax = sns.boxenplot(x="day", y="total_bill", hue="time",
                   data=tips, linewidth=2.5)
pp.savefig()
ax.figure.clear()

ax = sns.boxenplot(x="time", y="tip", data=tips,
                   order=["Dinner", "Lunch"])
pp.savefig()
ax.figure.clear()

iris = sns.load_dataset("iris")
print(iris.head())
ax = sns.boxenplot(data=iris, orient="h", palette="Set2")
pp.savefig()
ax.figure.clear()

ax = sns.boxenplot(x="day", y="total_bill", data=tips,
                   showfliers=False)
ax = sns.stripplot(x="day", y="total_bill", data=tips,
                   size=4, color=".26")
pp.savefig()
ax.figure.clear()

g = sns.catplot(x="sex", y="total_bill",
                hue="smoker", col="time",
                data=tips, kind="boxen",
                height=4, aspect=.7)
pp.savefig()
g.figure.clear()

pp.close()
