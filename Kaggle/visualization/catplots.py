#!/usr/bin/env python
# -*- coding: utf-8 -*-

import warnings
warnings.filterwarnings("ignore", message="Attempted to set non-positive left xlim on a log-scaled axis.\nInvalid limit will be ignored.")
import pandas as pd
pd.set_option("display.max_rows", 5)
pd.set_option("display.max_columns", 6)
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.max_open_warning': 0})
import seaborn as sns
sns.set_theme(style="ticks", color_codes=True)
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('catplots.pdf')
print("Setup Complete")

tips = sns.load_dataset("tips")
print(tips.head())
plot = sns.catplot(x="day", y="total_bill", data=tips)
pp.savefig()
plot.figure.clear()

plot = sns.catplot(x="day", y="total_bill", jitter=False, data=tips)
pp.savefig()
plot.figure.clear()

plot = sns.catplot(x="day", y="total_bill", kind="swarm", data=tips)
pp.savefig()
plot.figure.clear()

plot = sns.catplot(x="day", y="total_bill", hue="sex", kind="swarm", data=tips)
pp.savefig()
plot.figure.clear()

plot = sns.catplot(x="size", y="total_bill", data=tips)
pp.savefig()
plot.figure.clear()

plot = sns.catplot(x="smoker", y="tip", order=["No", "Yes"], data=tips)
pp.savefig()
plot.figure.clear()

plot = sns.catplot(x="total_bill", y="day", hue="time", kind="swarm", data=tips)
pp.savefig()
plot.figure.clear()

plot = sns.catplot(x="day", y="total_bill", kind="box", data=tips)
pp.savefig()
plot.figure.clear()

plot = sns.catplot(x="day", y="total_bill", hue="smoker", kind="box", data=tips)
pp.savefig()
plot.figure.clear()

tips["weekend"] = tips["day"].isin(["Sat", "Sun"])
plot = sns.catplot(x="day", y="total_bill", hue="weekend",
            kind="box", dodge=False, data=tips)
pp.savefig()
plot.figure.clear()

diamonds = sns.load_dataset("diamonds")
print(diamonds.head())
plot = sns.catplot(x="color", y="price", kind="boxen",
            data=diamonds.sort_values("color"))
pp.savefig()
plot.figure.clear()

plot = sns.catplot(x="total_bill", y="day", hue="sex",
            kind="violin", data=tips)
pp.savefig()
plot.figure.clear()

plot = sns.catplot(x="total_bill", y="day", hue="sex",
            kind="violin", bw=.15, cut=0,
            data=tips)
pp.savefig()
plot.figure.clear()

plot = sns.catplot(x="day", y="total_bill", hue="sex",
            kind="violin", split=True, data=tips)
pp.savefig()
plot.figure.clear()

plot = sns.catplot(x="day", y="total_bill", hue="sex",
            kind="violin", inner="stick", split=True,
            palette="pastel", data=tips)
pp.savefig()
plot.figure.clear()

g = sns.catplot(x="day", y="total_bill", kind="violin", inner=None, data=tips)
sns.swarmplot(x="day", y="total_bill", color="k", size=3, data=tips, ax=g.ax)
pp.savefig()
plot.figure.clear()

titanic = sns.load_dataset("titanic")
print(titanic.head())
plot = sns.catplot(x="sex", y="survived", hue="class", kind="bar", data=titanic)
pp.savefig()
plot.figure.clear()

plot = sns.catplot(x="deck", kind="count", palette="ch:.25", data=titanic)
pp.savefig()
plot.figure.clear()

plot = sns.catplot(y="deck", hue="class", kind="count",
            palette="pastel", edgecolor=".6",
            data=titanic)
pp.savefig()
plot.figure.clear()

plot = sns.catplot(x="sex", y="survived", hue="class", kind="point", data=titanic)
pp.savefig()
plot.figure.clear()

plot = sns.catplot(x="class", y="survived", hue="sex",
            palette={"male": "g", "female": "m"},
            markers=["^", "o"], linestyles=["-", "--"],
            kind="point", data=titanic)
pp.savefig()
plot.figure.clear()

g = sns.catplot(x="alive", col="deck", col_wrap=4,
                data=titanic[titanic.deck.notnull()],
                kind="count", height=2.5, aspect=.8)
pp.savefig()
plot.figure.clear()

g = sns.catplot(x="age", y="embark_town",
                hue="sex", row="class",
                data=titanic[titanic.embark_town.notnull()],
                orient="h", height=2, aspect=3, palette="Set3",
                kind="violin", dodge=True, cut=0, bw=.2)
pp.savefig()
plot.figure.clear()

g = sns.catplot(x="who", y="survived", col="class",
                data=titanic, saturation=.5,
                kind="bar", ci=None, aspect=.6)
(g.set_axis_labels("", "Survival Rate")
  .set_xticklabels(["Men", "Women", "Children"])
  .set_titles("{col_name} {col_var}")
  .set(ylim=(0, 1))
  .despine(left=True))
pp.savefig()
plot.figure.clear()

iris = sns.load_dataset("iris")
print(iris.head())
plot = sns.catplot(data=iris, orient="h", kind="box")
pp.savefig()
plot.figure.clear()

plot =  sns.violinplot(x=iris.species, y=iris.sepal_length)
pp.savefig()
plot.figure.clear()

f, ax = plt.subplots(figsize=(7, 3))
plot = sns.countplot(y="deck", data=titanic, color="c")
pp.savefig()
f.figure.clear()

plot = sns.catplot(x="day", y="total_bill", hue="smoker",
            col="time", aspect=.7,
            kind="swarm", data=tips)
pp.savefig()
f.figure.clear()

g = sns.catplot(x="fare", y="survived", row="class",
                kind="box", orient="h", height=1.5, aspect=4,
                data=titanic.query("fare > 0"))
g.set(xscale="log")
pp.savefig()
g.figure.clear()

exercise = sns.load_dataset("exercise")
print(exercise.head())
g = sns.catplot(x="time", y="pulse", hue="kind", data=exercise)
pp.savefig()
g.figure.clear()

g = sns.catplot(x="time", y="pulse", hue="kind",
               data=exercise, kind="violin")
pp.savefig()
g.figure.clear()

g = sns.catplot(x="time", y="pulse", hue="kind",
                col="diet", data=exercise)
pp.savefig()
g.figure.clear()

g = sns.catplot(x="time", y="pulse", hue="kind",
                col="diet", data=exercise,
                height=5, aspect=.8)
pp.savefig()
g.figure.clear()

pp.close()
