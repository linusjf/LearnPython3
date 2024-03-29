#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages("custom.pdf")
print("Setup Complete")

# Create a figure of size 8x6 inches, 80 dots per inch
plt.figure(figsize=(8, 6), dpi=80)
# Create a new subplot from a grid of 1x1
plt.subplot(1, 1, 1)
X = np.linspace(-np.pi, np.pi, 256)
C, S = np.cos(X), np.sin(X)
plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="sine")
plt.plot(X, S, color="green", linewidth=2.5, linestyle="-", label="cosine")
plt.legend(loc="upper left")
# Set x limits
plt.xlim(X.min() * 1.1, X.max() * 1.1)
# Set x ticks
plt.xticks(
    [-np.pi, -np.pi / 2, np.pi / 2, np.pi], [r"$-\pi$", r"$-\pi/2$", r"$+\pi/2$", r"$+\pi$"]
)
# Set y limits
plt.ylim(C.min() * 1.1, C.max() * 1.1)
# Set y ticks
plt.yticks([-1, +1], [r"$-1$", r"$+1$"])
# move spine
# gca stands for 'get current axis'
ax = plt.gca()
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")
ax.xaxis.set_ticks_position("bottom")
ax.spines["bottom"].set_position(("data", 0))
ax.yaxis.set_ticks_position("left")
ax.spines["left"].set_position(("data", 0))

# Annotate
t = 2 * np.pi / 3
plt.plot([t, t], [0, np.cos(t)], color="blue", linewidth=2.5, linestyle="--")
plt.scatter(
    [
        t,
    ],
    [
        np.cos(t),
    ],
    50,
    color="blue",
)
plt.annotate(
    r"$cos(\frac{2\pi}{3} )=-\frac{1} {2} $",
    xy=(t, np.cos(t)),
    xycoords="data",
    xytext=(-90, -50),
    textcoords="offset points",
    fontsize=16,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
plt.plot([t, t], [0, np.sin(t)], color="red", linewidth=2.5, linestyle="--")
plt.scatter(
    [
        t,
    ],
    [
        np.sin(t),
    ],
    50,
    color="red",
)
plt.annotate(
    r"$sin(\frac{2\pi}{3} )=\frac{\sqrt{3} }{2} $",
    xy=(t, np.sin(t)),
    xycoords="data",
    xytext=(+10, +30),
    textcoords="offset points",
    fontsize=16,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)

# resize ticks
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor="white", edgecolor="None", alpha=0.65))

# Save figure using 72 dots per inch
plt.savefig("custom.png", dpi=72)
# Show result on screen
plt.show()
pp.savefig()
pp.close()
