#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages("pcadigits.pdf")
print("Setup Complete")
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA

digits = load_digits()
print(digits.data.shape)
# project from 64 to 2 dimensions
pca = PCA(2)
projected = pca.fit_transform(digits.data)
print(digits.data.shape)
print(projected.shape)
plt.scatter(
    projected[:, 0],
    projected[:, 1],
    c=digits.target,
    edgecolor="none",
    alpha=0.5,
    cmap=plt.cm.get_cmap("nipy_spectral", 10),
)
plt.xlabel("component 1")
plt.ylabel("component 2")
plt.colorbar()
pp.savefig()
plt.clf()

pca = PCA().fit(digits.data)
plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel("number of components")
plt.ylabel("cumulative explained variance")
pp.savefig()
plt.clf()


def plot_digits(data):
    fig, axes = plt.subplots(
        4,
        10,
        figsize=(10, 4),
        subplot_kw={"xticks": [], "yticks": []},
        gridspec_kw=dict(hspace=0.1, wspace=0.1),
    )
    for i, ax in enumerate(axes.flat):
        ax.imshow(data[i].reshape(8, 8), cmap="binary", interpolation="nearest", clim=(0, 16))


plot_digits(digits.data)
pp.savefig()
plt.clf()

np.random.seed(42)
noisy = np.random.normal(digits.data, 4)
plot_digits(noisy)
pp.savefig()
plt.clf()

pca = PCA(0.50).fit(noisy)
print(pca.n_components_)

components = pca.transform(noisy)
filtered = pca.inverse_transform(components)
plot_digits(filtered)
pp.savefig()
plt.clf()
pp.close()
