#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

pd.set_option("display.max_rows", 5)
pd.set_option("display.max_columns", 6)
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages("barchart.pdf")
print("Setup Complete")

sns.set_theme(style="whitegrid")
tips = sns.load_dataset("tips")
print(tips.head())
plot = sns.barplot(x="day", y="total_bill", data=tips)
plot.set_title("Fig 1")
pp.savefig()
plot.get_figure().clf()

plot = sns.barplot(x="day", y="total_bill", hue="sex", data=tips)
plot.set_title("Fig 2")
pp.savefig()
plot.get_figure().clf()

plot = sns.barplot(x="tip", y="day", data=tips)
plot.set_title("Fig 3")
pp.savefig()
plot.get_figure().clf()

plot = sns.barplot(x="time", y="tip", data=tips, order=["Dinner", "Lunch"])
plot.set_title("Fig 4")
pp.savefig()
plot.get_figure().clf()

from numpy import median

plot = sns.barplot(x="day", y="tip", data=tips, estimator=median)
plot.set_title("Fig 5")
pp.savefig()
plot.get_figure().clf()

plot = sns.barplot(x="day", y="tip", data=tips, ci=68)
plot.set_title("Fig 6")
pp.savefig()
plot.get_figure().clf()

plot = sns.barplot(x="day", y="tip", data=tips, ci="sd")
plot.set_title("Fig 6")
pp.savefig()
plot.get_figure().clf()

plot = sns.barplot(x="day", y="tip", data=tips, capsize=0.2)
plot.set_title("Fig 7")
pp.savefig()
plot.get_figure().clf()

plot = sns.barplot(x="size", y="total_bill", data=tips, palette="Blues_d")
plot.set_title("Fig 8")
pp.savefig()
plot.get_figure().clf()

tips["weekend"] = tips["day"].isin(["Sat", "Sun"])
plot = sns.barplot(x="day", y="total_bill", hue="weekend", data=tips, dodge=False)
plot.set_title("Fig 9")
pp.savefig()
plot.get_figure().clf()

plot = sns.barplot(x="size", y="total_bill", data=tips, color="salmon", saturation=0.5)
plot.set_title("Fig 10")
pp.savefig()
plot.get_figure().clf()

plot = sns.barplot(
    x="day",
    y="total_bill",
    data=tips,
    linewidth=2.5,
    facecolor=(1, 1, 1, 0),
    errcolor=".2",
    edgecolor=".2",
)
plot.set_title("Fig 11")
pp.savefig()
plot.get_figure().clf()

g = sns.catplot(
    x="sex", y="total_bill", hue="smoker", col="time", data=tips, kind="bar", height=4, aspect=0.7
)
g.fig.suptitle("Fig 12")
pp.savefig()

pp.close()
