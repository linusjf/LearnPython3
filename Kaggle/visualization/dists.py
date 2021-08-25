#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
pd.set_option("display.max_rows", 5)
pd.set_option("display.max_columns", 6)
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('dists.pdf')
print("Setup Complete")

penguins = sns.load_dataset("penguins")
plot = sns.displot(data=penguins, x="flipper_length_mm")
plot.figure.suptitle("Fig 1")
pp.savefig()
plot.figure.clear()

plot = sns.displot(data=penguins, x="flipper_length_mm", kind="kde")
plot.figure.suptitle("Fig 2")
pp.savefig()
plot.figure.clear()

plot = sns.displot(data=penguins, x="flipper_length_mm", kind="ecdf")
plot.figure.suptitle("Fig 3")
pp.savefig()
plot.figure.clear()

plot = sns.displot(data=penguins, x="flipper_length_mm", kde=True)
plot.figure.suptitle("Fig 4")
pp.savefig()
plot.figure.clear()

plot = sns.displot(data=penguins, x="flipper_length_mm", y="bill_length_mm")
plot.figure.suptitle("Fig 5")
pp.savefig()
plot.figure.clear()

plot = sns.displot(data=penguins, x="flipper_length_mm", y="bill_length_mm", kind="kde")
plot.figure.suptitle("Fig 6")
pp.savefig()
plot.figure.clear()

plot = sns.displot(data=penguins, x="flipper_length_mm", y="bill_length_mm", kind="kde", rug=True)
plot.figure.suptitle("Fig 7")
pp.savefig()
plot.figure.clear()

plot = sns.displot(data=penguins, x="flipper_length_mm", hue="species", kind="kde")
plot.figure.suptitle("Fig 8")
pp.savefig()
plot.figure.clear()

plot = sns.displot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack")
plot.figure.suptitle("Fig 9")
pp.savefig()
plot.figure.clear()

plot = sns.displot(data=penguins, x="flipper_length_mm", hue="species", col="sex", kind="kde")
plot.figure.suptitle("Fig 10")
pp.savefig()
plot.figure.clear()

plot = sns.displot(
    data=penguins, y="flipper_length_mm", hue="sex", col="species",
    kind="ecdf", height=4, aspect=.7,
)
plot.figure.suptitle("Fig 11")
pp.savefig()
plot.figure.clear()

plot = sns.displot(
    data=penguins, y="flipper_length_mm", hue="sex", col="species",
    kind="ecdf", height=4, aspect=.7,
)
plot.figure.suptitle("Fig 12")
pp.savefig()
plot.figure.clear()

g = sns.displot(
    data=penguins, y="flipper_length_mm", hue="sex", col="species",
    kind="kde", height=4, aspect=.7,
)
g.set_axis_labels("Density (a.u.)", "Flipper length (mm)")
g.set_titles("{col_name} penguins")
pp.savefig()
g.figure.clear()

pp.close()
