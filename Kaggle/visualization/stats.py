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

plot = sns.relplot(x="timepoint", y="signal", hue="event", kind="line", data=fmri);
pp.savefig()
plot.figure.clear()

plot = sns.relplot(x="timepoint", y="signal", hue="region", style="event",
            kind="line", data=fmri);
pp.savefig()
plot.figure.clear()

plot = sns.relplot(x="timepoint", y="signal", hue="region", style="event",
            dashes=False, markers=True, kind="line", data=fmri);
pp.savefig()
plot.figure.clear()

plot = sns.relplot(x="timepoint", y="signal", hue="event", style="event",
            kind="line", data=fmri);
pp.savefig()
plot.figure.clear()

plot = sns.relplot(x="timepoint", y="signal", hue="region",
            units="subject", estimator=None,
            kind="line", data=fmri.query("event == 'stim'"));
pp.savefig()
plot.figure.clear()

dots = sns.load_dataset("dots").query("align == 'dots'")
plot = sns.relplot(x="time", y="firing_rate",
            hue="coherence", style="choice",
            kind="line", data=dots);
pp.savefig()
plot.figure.clear()

palette = sns.cubehelix_palette(light=.8, n_colors=6)
plot = sns.relplot(x="time", y="firing_rate",
            hue="coherence", style="choice",
            palette=palette,
            kind="line", data=dots);
pp.savefig()
plot.figure.clear()

from matplotlib.colors import LogNorm
palette = sns.cubehelix_palette(light=.7, n_colors=6)
plot = sns.relplot(x="time", y="firing_rate",
            hue="coherence", style="choice",
            hue_norm=LogNorm(),
            kind="line",
            data=dots.query("coherence > 0"));
pp.savefig()
plot.figure.clear()

plot = sns.relplot(x="time", y="firing_rate",
            size="coherence", style="choice",
            kind="line", data=dots);
pp.savefig()
plot.figure.clear()

plot = sns.relplot(x="time", y="firing_rate",
           hue="coherence", size="choice",
           palette=palette,
           kind="line", data=dots);
pp.savefig()
plot.figure.clear()

df = pd.DataFrame(dict(time=pd.date_range("2017-1-1", periods=500),
                       value=np.random.randn(500).cumsum()))
g = sns.relplot(x="time", y="value", kind="line", data=df)
g.figure.autofmt_xdate()
pp.savefig()
g.figure.clear()

plot = sns.relplot(x="total_bill", y="tip", hue="smoker",
            col="time", data=tips);
pp.savefig()
plot.figure.clear()

plot = sns.relplot(x="timepoint", y="signal", hue="subject",
            col="region", row="event", height=3,
            kind="line", estimator=None, data=fmri);
pp.savefig()
plot.figure.clear()

plot = sns.relplot(x="timepoint", y="signal", hue="event", style="event",
            col="subject", col_wrap=5,
            height=3, aspect=.75, linewidth=2.5,
            kind="line", data=fmri.query("region == 'frontal'"));
pp.savefig()
plot.figure.clear()

pp.close()
