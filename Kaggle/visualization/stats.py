#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
pd.set_option("display.max_rows", 5)
pd.set_option("display.max_columns", 6)
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="darkgrid")
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('stats.pdf')
print("Setup Complete")

tips = sns.load_dataset("tips")
plot = sns.relplot(x="total_bill", y="tip", data=tips);
pp.savefig()
plot.figure.clear()

plot = sns.relplot(x="total_bill", y="tip", hue="smoker", data=tips);
pp.savefig()
plot.figure.clear()

plot = sns.relplot(x="total_bill", y="tip", hue="smoker", style="smoker",
            data=tips);
pp.savefig()
plot.figure.clear()

plot = sns.relplot(x="total_bill", y="tip", hue="smoker", style="time", data=tips);
pp.savefig()
plot.figure.clear()

plot = sns.relplot(x="total_bill", y="tip", hue="size", data=tips);
pp.savefig()
plot.figure.clear()

plot = sns.relplot(x="total_bill", y="tip", hue="size", palette="ch:r=-.5,l=.75", data=tips);
pp.savefig()
plot.figure.clear()

plot = sns.relplot(x="total_bill", y="tip", size="size", data=tips);
pp.savefig()
plot.figure.clear()

plot = sns.relplot(x="total_bill", y="tip", size="size", sizes=(15, 200), data=tips);
pp.savefig()
plot.figure.clear()

df = pd.DataFrame(dict(time=np.arange(500),
                       value=np.random.randn(500).cumsum()))
g = sns.relplot(x="time", y="value", kind="line", data=df)
g.figure.autofmt_xdate()
pp.savefig()
g.figure.clear()

df = pd.DataFrame(np.random.randn(500, 2).cumsum(axis=0), columns=["x", "y"])
plot = sns.relplot(x="x", y="y", sort=False, kind="line", data=df);
pp.savefig()
plot.figure.clear()

fmri = sns.load_dataset("fmri")
plot = sns.relplot(x="timepoint", y="signal", kind="line", data=fmri);
pp.savefig()
plot.figure.clear()

plot = sns.relplot(x="timepoint", y="signal", ci=None, kind="line", data=fmri);
pp.savefig()
plot.figure.clear()

plot = sns.relplot(x="timepoint", y="signal", kind="line", ci="sd", data=fmri);
pp.savefig()
plot.figure.clear()

plot = sns.relplot(x="timepoint", y="signal", estimator=None, kind="line", data=fmri);
pp.savefig()
plot.figure.clear()

pp.close()
