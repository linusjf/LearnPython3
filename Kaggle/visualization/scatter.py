#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
pd.set_option("display.max_rows", 5)
pd.set_option("display.max_columns", 6)
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('scatter.pdf')
print("Setup Complete")

tips = sns.load_dataset("tips")
print(tips.head())

plot = sns.scatterplot(data=tips, x="total_bill", y="tip")
plot.set_title("Fig 1")
pp.savefig()
plot.get_figure().clf()

plot = sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time")
plot.set_title("Fig 2")
pp.savefig()
plot.get_figure().clf()

plot = sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", style="time")
plot.set_title("Fig 3")
pp.savefig()
plot.get_figure().clf()

plot = sns.scatterplot(data=tips, x="total_bill", y="tip", hue="day", style="time")
plot.set_title("Fig 4")
pp.savefig()
plot.get_figure().clf()

plot = sns.scatterplot(data=tips, x="total_bill", y="tip", hue="size")
plot.set_title("Fig 5")
pp.savefig()
plot.get_figure().clf()

plot = sns.scatterplot(data=tips, x="total_bill", y="tip", hue="size", palette="deep")
plot.set_title("Fig 6")
pp.savefig()
plot.get_figure().clf()

tip_rate = tips.eval("tip / total_bill").rename("tip_rate")
plot = sns.scatterplot(data=tips, x="total_bill", y="tip", hue=tip_rate)
plot.set_title("Fig 7")
pp.savefig()
plot.get_figure().clf()

plot = sns.scatterplot(data=tips, x="total_bill", y="tip", hue="size", size="size")
plot.set_title("Fig 8")
pp.savefig()
plot.get_figure().clf()

plot = sns.scatterplot(
    data=tips, x="total_bill", y="tip", hue="size", size="size",
    sizes=(20, 200), legend="full"
)
plot.set_title("Fig 9")
pp.savefig()
plot.get_figure().clf()

plot = sns.scatterplot(
    data=tips, x="total_bill", y="tip", hue="size", size="size",
    sizes=(20, 200), hue_norm=(0, 7), legend="full"
)
plot.set_title("Fig 10")
pp.savefig()
plot.get_figure().clf()

markers = {"Lunch": "s", "Dinner": "X"}
plot = sns.scatterplot(data=tips, x="total_bill", y="tip", style="time", markers=markers)
plot.set_title("Fig 11")
pp.savefig()
plot.get_figure().clf()

plot = sns.scatterplot(data=tips, x="total_bill", y="tip", s=100, color=".2", marker="+")
plot.set_title("Fig 12")
pp.savefig()
plot.get_figure().clf()

facet = sns.relplot(
    data=tips, x="total_bill", y="tip",
    col="time", hue="day", style="day",
    kind="scatter"
)
facet.figure.suptitle("Facet Grid (time)")
pp.savefig()

facet = sns.relplot(
    data=tips, x="total_bill", y="tip",
    col="day", hue="time", style="time",
    kind="scatter"
)
facet.figure.suptitle("Facet Grid (day)")
pp.savefig()
facet.figure.clear()

index = pd.date_range("1 1 2000", periods=100, freq="m", name="date")
data = np.random.randn(100, 4).cumsum(axis=0)
wide_df = pd.DataFrame(data, index, ["a", "b", "c", "d"])
plot = sns.scatterplot(data=wide_df)
plot.set_title("Fig 15")
pp.savefig()
plot.get_figure().clf()

pp.close()
