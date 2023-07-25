#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages("eigenfaces.pdf")
print("Setup Complete")

from sklearn.datasets import fetch_lfw_people
from sklearn.decomposition import PCA as RandomizedPCA

faces = fetch_lfw_people(min_faces_per_person=60)
print(faces.target_names)
print(faces.images.shape)
pca = RandomizedPCA(150, svd_solver="randomized")
pca.fit(faces.data)
RandomizedPCA(
    copy=True,
    iterated_power=3,
    n_components=150,
    svd_solver="randomized",
    random_state=None,
    whiten=False,
)

fig, axes = plt.subplots(
    3,
    8,
    figsize=(9, 4),
    subplot_kw={"xticks": [], "yticks": []},
    gridspec_kw=dict(hspace=0.1, wspace=0.1),
)
for i, ax in enumerate(axes.flat):
    ax.imshow(pca.components_[i].reshape(62, 47), cmap="bone")
pp.savefig()
plt.clf()

plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel("number of components")
plt.ylabel("cumulative explained variance")
pp.savefig()
plt.clf()

# Compute the components and projected faces
pca = RandomizedPCA(150, svd_solver="randomized").fit(faces.data)
components = pca.transform(faces.data)
projected = pca.inverse_transform(components)
# Plot the results
fig, ax = plt.subplots(
    2,
    10,
    figsize=(10, 2.5),
    subplot_kw={"xticks": [], "yticks": []},
    gridspec_kw=dict(hspace=0.1, wspace=0.1),
)
for i in range(10):
    ax[0, i].imshow(faces.data[i].reshape(62, 47), cmap="binary_r")
    ax[1, i].imshow(projected[i].reshape(62, 47), cmap="binary_r")

ax[0, 0].set_ylabel("full-dim\ninput")
ax[1, 0].set_ylabel("150-dim\nreconstruction")
pp.savefig()
plt.clf()
pp.close()
