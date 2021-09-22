#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
from scipy.sparse.csgraph import dijkstra
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse.csgraph import breadth_first_order
from scipy.sparse.csgraph import depth_first_order

arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])

newarr = csr_matrix(arr)

print(connected_components(newarr))
print(dijkstra(newarr, return_predecessors=True, indices=0))
print(floyd_warshall(newarr, return_predecessors=True))
print(bellman_ford(newarr, return_predecessors=True, indices=0))
print(breadth_first_order(newarr, 1))
