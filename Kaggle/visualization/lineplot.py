#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
pd.set_option("display.max_rows", 5)
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('lineplot.pdf')
print("Setup Complete")

flights = sns.load_dataset("flights")
print(flights.head())

may_flights = flights.query("month == 'May'")
plot = sns.lineplot(data=may_flights, x="year", y="passengers")
plot.set_title("Fig 1")
pp.savefig()
plot.get_figure().clf()

flights_wide = flights.pivot("year", "month", "passengers")
print(flights_wide.head())

plot = sns.lineplot(data=flights_wide["May"])
plot.set_title("Fig 2")
pp.savefig()
plot.get_figure().clf()

plot = sns.lineplot(data=flights_wide)
plot.set_title("Fig 3")
pp.savefig()
plot.get_figure().clf()

plot = sns.lineplot(data=flights, x="year", y="passengers")
plot.set_title("Fig 4")
pp.savefig()
plot.get_figure().clf()

plot = sns.lineplot(data=flights, x="year", y="passengers", hue="month")
plot.set_title("Fig 5")
pp.savefig()
plot.get_figure().clf()

plot = sns.lineplot(data=flights, x="year", y="passengers", hue="month", style="month")
plot.set_title("Fig 6")
pp.savefig()
plot.get_figure().clf()

fmri = sns.load_dataset("fmri")
print(fmri.head())

plot = sns.lineplot(data=fmri, x="timepoint", y="signal", hue="event")
plot.set_title("Fig 7")
pp.savefig()
plot.get_figure().clf()

plot = sns.lineplot(data=fmri, x="timepoint", y="signal", hue="region", style="event")
plot.set_title("Fig 8")
pp.savefig()
plot.get_figure().clf()

plot = sns.lineplot(
    data=fmri,
    x="timepoint", y="signal", hue="event", style="event",
    markers=True, dashes=False
)
plot.set_title("Fig 9")
pp.savefig()
plot.get_figure().clf()

plot = sns.lineplot(
    data=fmri, x="timepoint", y="signal", hue="event", err_style="bars", ci=68
)
plot.set_title("Fig 10")
pp.savefig()
plot.get_figure().clf()

plot = sns.lineplot(
    data=fmri.query("region == 'frontal'"),
    x="timepoint", y="signal", hue="event", units="subject",
    estimator=None, lw=1,
)
plot.set_title("Fig 11")
pp.savefig()
plot.get_figure().clf()

pp.close()
