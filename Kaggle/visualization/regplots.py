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
pp = PdfPages('regplots.pdf')
print("Setup Complete")

tips = sns.load_dataset("tips")
plot = sns.regplot(x="total_bill", y="tip", data=tips);
pp.savefig()
plot.figure.clear()

plot = sns.lmplot(x="total_bill", y="tip", data=tips);
pp.savefig()
plot.figure.clear()

plot = sns.lmplot(x="size", y="tip", data=tips);
pp.savefig()
plot.figure.clear()

plot = sns.lmplot(x="size", y="tip", data=tips, x_jitter=.05);
pp.savefig()
plot.figure.clear()

plot = sns.lmplot(x="size", y="tip", data=tips, x_estimator=np.mean);
pp.savefig()
plot.figure.clear()

anscombe = sns.load_dataset("anscombe")
plot = sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'I'"),
           ci=None, scatter_kws={"s": 80});
pp.savefig()
plot.figure.clear()

plot = sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'II'"),
           ci=None, scatter_kws={"s": 80});
pp.savefig()
plot.figure.clear()

plot = sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'II'"),
           order=2, ci=None, scatter_kws={"s": 80});
pp.savefig()
plot.figure.clear()

plot = sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'III'"),
           ci=None, scatter_kws={"s": 80});
pp.savefig()
plot.figure.clear()

plot = sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'III'"),
           robust=True, ci=None, scatter_kws={"s": 80});
pp.savefig()
plot.figure.clear()

tips["big_tip"] = (tips.tip / tips.total_bill) > .15
plot = sns.lmplot(x="total_bill", y="big_tip", data=tips,
           y_jitter=.03);
pp.savefig()
plot.figure.clear()

plot = sns.lmplot(x="total_bill", y="big_tip", data=tips,
           logistic=True, y_jitter=.03);
pp.savefig()
plot.figure.clear()

plot = sns.lmplot(x="total_bill", y="tip", data=tips,
           lowess=True);
pp.savefig()
plot.figure.clear()

plot = sns.residplot(x="x", y="y", data=anscombe.query("dataset == 'I'"),
              scatter_kws={"s": 80});
pp.savefig()
plot.figure.clear()

plot = sns.residplot(x="x", y="y", data=anscombe.query("dataset == 'II'"),
              scatter_kws={"s": 80});
pp.savefig()
plot.figure.clear()

plot = sns.lmplot(x="total_bill", y="tip", hue="smoker", data=tips);
pp.savefig()
plot.figure.clear()

plot = sns.lmplot(x="total_bill", y="tip", hue="smoker", data=tips,
           markers=["o", "x"], palette="Set1");
pp.savefig()
plot.figure.clear()

plot = sns.lmplot(x="total_bill", y="tip", hue="smoker", col="time", data=tips);
pp.savefig()
plot.figure.clear()

plot = sns.lmplot(x="total_bill", y="tip", hue="smoker",
           col="time", row="sex", data=tips);
pp.savefig()
plot.figure.clear()

f, ax = plt.subplots(figsize=(5, 6))
plot = sns.regplot(x="total_bill", y="tip", data=tips, ax=ax);
pp.savefig()
f.figure.clear()

plot = sns.lmplot(x="total_bill", y="tip", col="day", data=tips,
           col_wrap=2, height=3);
pp.savefig()
plot.figure.clear()

plot = sns.lmplot(x="total_bill", y="tip", col="day", data=tips,
           aspect=.5);
pp.savefig()
plot.figure.clear()

plot = sns.jointplot(x="total_bill", y="tip", data=tips, kind="reg");
pp.savefig()
plot.figure.clear()

plot = sns.pairplot(tips, x_vars=["total_bill", "size"], y_vars=["tip"],
             height=5, aspect=.8, kind="reg");
pp.savefig()
plot.figure.clear()

plot = sns.pairplot(tips, x_vars=["total_bill", "size"], y_vars=["tip"],
             hue="smoker", height=5, aspect=.8, kind="reg")
pp.savefig()
plot.figure.clear()

pp.close()
