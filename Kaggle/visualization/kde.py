#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
pd.set_option("display.max_rows", 5)
pd.set_option("display.max_columns", 6)
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('kde.pdf')
print("Setup Complete")

tips = sns.load_dataset("tips")
print(tips.head())
plot = sns.kdeplot(data=tips, x="total_bill")
plot.set_title("Total Bill density function")
pp.savefig()
plot.figure.clear()

plot = sns.kdeplot(data=tips, y="total_bill")
plot.set_title("Total Bill density function (Vertical)")
pp.savefig()
plot.figure.clear()

iris = sns.load_dataset("iris")
print(iris.head())
plot = sns.kdeplot(data=iris)
plot.set_title("Iris density plots")
pp.savefig()
plot.figure.clear()

plot = sns.kdeplot(data=tips, x="total_bill", bw_adjust=.2)
plot.set_title("Total bill density smoothed less")
pp.savefig()
plot.figure.clear()

plot = sns.kdeplot(data=tips, x="total_bill", bw_adjust=5, cut=0)
plot.set_title("Total bill density smoothed more")
pp.savefig()
plot.figure.clear()

plot = sns.kdeplot(data=tips, x="total_bill", hue="time")
plot.set_title("Total bill at times")
pp.savefig()
plot.figure.clear()

plot = sns.kdeplot(data=tips, x="total_bill", hue="time", multiple="stack")
plot.set_title("Total bill density stacked")
pp.savefig()
plot.figure.clear()

plot = sns.kdeplot(data=tips, x="total_bill", hue="time", multiple="fill")
plot.set_title("Total bill density filled")
pp.savefig()
plot.figure.clear()

plot = sns.kdeplot(
    data=tips, x="total_bill", hue="time",
    cumulative=True, common_norm=False, common_grid=True,
)
plot.set_title("Total bill density cumulative")
pp.savefig()
plot.figure.clear()

tips_agg = (tips
    .groupby("size")
    .agg(total_bill=("total_bill", "mean"), n=("total_bill", "count"))
)
print(tips_agg.head())
plot = sns.kdeplot(data=tips_agg, x="total_bill", weights="n")
plot.set_title("Aggregate tips density")
pp.savefig()
plot.figure.clear()

diamonds = sns.load_dataset("diamonds")
print(diamonds.head())
plot = sns.kdeplot(data=diamonds, x="price", log_scale=True)
plot.set_title("Diamonds price density")
pp.savefig()
plot.figure.clear()

plot = sns.kdeplot(data=tips, x="total_bill", hue="size")
plot.set_title("Total bill density by size")
pp.savefig()
plot.figure.clear()

plot = sns.kdeplot(
   data=tips, x="total_bill", hue="size",
   fill=True, common_norm=False, palette="crest",
   alpha=.5, linewidth=0,
)
plot.set_title("Total bill density (palette)")
pp.savefig()
plot.figure.clear()

geyser = sns.load_dataset("geyser")
print(geyser.head())
plot = sns.kdeplot(data=geyser, x="waiting", y="duration")
plot.set_title("Geyser Bivariate plot")
pp.savefig()
plot.figure.clear()

plot = sns.kdeplot(data=geyser, x="waiting", y="duration", hue="kind")
plot.set_title("Geyser Bivariate Hues")
pp.savefig()
plot.figure.clear()

plot = sns.kdeplot(
    data=geyser, x="waiting", y="duration", hue="kind", fill=True,
)
plot.set_title("Geyser Bivariate Hues")
pp.savefig()
plot.figure.clear()

plot = sns.kdeplot(
    data=geyser, x="waiting", y="duration", hue="kind", fill=True,
)
plot.set_title("Geyser Bivariate Contours")
pp.savefig()
plot.figure.clear()

plot = sns.kdeplot(
    data=geyser, x="waiting", y="duration", hue="kind",
    levels=5, thresh=.2,
)
plot.set_title("Geyser Bivariate Less Contours")
pp.savefig()
plot.figure.clear()

plot = sns.kdeplot(
    data=geyser, x="waiting", y="duration",
    fill=True, thresh=0, levels=100, cmap="mako",
)
plot.set_title("Geyser Bivariate ColorMap")
pp.savefig()
plot.figure.clear()
pp.close()
