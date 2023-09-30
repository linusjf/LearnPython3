#!/usr/bin/env python
"""
Distortion.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : distortion
# @created     : Saturday Sep 30, 2023 09:38:20 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages("distortion.pdf")
print("Setup Complete")

# Constant used several times below.
NUM_CLUSTERS = 3

# Create the test data. Only the data in X is used.
X, y = make_blobs(n_samples=20,
                  n_features=2,
                  centers=NUM_CLUSTERS,
                  cluster_std=0.9,
                  shuffle=True,
                  random_state=44)

# Cluster scatterplot without centroids.
plt.scatter(X[:, 0], X[:, 1], c='green', marker='o', s=30)
plt.grid()
# plt.tight_layout()
pp.savefig()
plt.clf()

print("\nNOTE: Each centroid below is the final one chosen after k-means runs max_iter times.")

SAVED_INERTIA = []

# Loop through max number of clusters. Add a few additional clusters
# beyond the constant specified so the elbow can be seen.
for cluster_count in range(1, NUM_CLUSTERS+3):
    # BEGIN INDENT HERE…
    km = KMeans(n_clusters=cluster_count,
                init='random',
                n_init=10,
                max_iter=200,
                random_state=0)
    km.fit(X)

    # Save the distortion for each final cluster chosen by KMeans above.
    SAVED_INERTIA.append(km.inertia_)

    # Show the dots.
    plt.scatter(X[:, 0],
                X[:, 1],
                c='green',
                marker='o',
                s=30)

    # Show the Centroids.
    plt.scatter(km.cluster_centers_[:, 0],
                km.cluster_centers_[:, 1],
                s=250,
                marker='+',
                c='red',
                label='Centroid')

    plt.title("Within cluster SSE (aka distortion): %.2f" % km.inertia_)
    plt.legend()
    plt.grid()
    plt.tight_layout()
    pp.savefig()
    plt.clf()

    # END INDENT

# Plot the line graph with the elbow.
plt.plot(range(1, NUM_CLUSTERS+3), SAVED_INERTIA, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Within cluster SSE (aka distortion)')
plt.tight_layout()
pp.savefig()
plt.clf()
pp.close()
