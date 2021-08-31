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
sns.set_theme(style="whitegrid")
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('swarmplots.pdf')
print("Setup Complete")

tips = sns.load_dataset("tips")
print(tips.head())
ax = sns.swarmplot(x=tips["total_bill"])
pp.savefig()
ax.figure.clear()

ax = sns.swarmplot(x="day", y="total_bill", data=tips)
pp.savefig()
ax.figure.clear()

ax = sns.swarmplot(x="total_bill", y="day", data=tips)
pp.savefig()
ax.figure.clear()

ax = sns.swarmplot(x="day", y="total_bill", hue="sex", data=tips)
pp.savefig()
ax.figure.clear()

ax = sns.swarmplot(x="day", y="total_bill", hue="smoker",
                   data=tips, palette="Set2", dodge=True)
pp.savefig()
ax.figure.clear()

ax = sns.swarmplot(x="time", y="total_bill", data=tips,
                   order=["Dinner", "Lunch"])
pp.savefig()
ax.figure.clear()

ax = sns.swarmplot(x="time", y="total_bill", data=tips, size=6)
pp.savefig()
ax.figure.clear()

ax = sns.boxplot(x="total_bill", y="day", data=tips, whis=np.inf)
ax = sns.swarmplot(x="total_bill", y="day", data=tips, color=".2")
pp.savefig()
ax.figure.clear()

ax = sns.violinplot(x="day", y="total_bill", data=tips, inner=None)
ax = sns.swarmplot(x="day", y="total_bill", data=tips,
                   color="white", edgecolor="gray")
pp.savefig()
ax.figure.clear()

g = sns.catplot(x="sex", y="total_bill",
                hue="smoker", col="time",
                data=tips, kind="swarm",
                height=4, aspect=.7);
pp.savefig()
g.figure.clear()

pp.close()
