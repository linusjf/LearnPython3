#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scipy.cluster.vq import kmeans, vq, whiten
from numpy import vstack, array
from numpy.random import rand

# data generation with three features
data = vstack((rand(100, 3) + array([0.5, 0.5, 0.5]), rand(100, 3)))

print(data.shape)

# whitening of data
data = whiten(data)
# computing K-Means with K = 3 (2 clusters)
centroids, _ = kmeans(data, 3)

print(centroids)

# assign each sample to a cluster
clx, _ = vq(data, centroids)
print(clx)
