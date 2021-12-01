#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021  <@localhost>
#
# Distributed under terms of the MIT license.

"""

"""
from math import log

def arbitrage(graph):
    transformed_graph = [[-log(edge) for edge in row] for row in graph]

    # Pick any source vertex -- we can run Bellman-Ford from any vertex and
    # get the right result
    source = 0
    n = len(transformed_graph)
    min_dist = [float('inf')] * n

    min_dist[source] = 0

    # Relax edges |V - 1| times
    for i in range(n - 1):
        for v in range(n):
            for w in range(n):
                if min_dist[w] > min_dist[v] + transformed_graph[v][w]:
                    min_dist[w] = min_dist[v] + transformed_graph[v][w]

    # If we can still relax edges, then we have a negative cycle
    for v in range(n):
        for w in range(n):
            if min_dist[w] > min_dist[v] + transformed_graph[v][w]:
                return True

    return False

curr_rates = [[1,	0.8825,	0.7510,	113.37,	0.9204,	1.2743,	1.3970],
              [1.1331,	1,	0.8510,	128.47,	1.0429,	1.4439,	1.5830],
              [1.3314,	1.1751,	1,	150.94,	1.2255,	1.6966,	1.8601],
              [0.882050,0.77845,0.00663,1,0.8118,0.01124,0.01232],
              [1.0865,0.9588,0.8160,123.18,1,1.3845,1.5178],
              [0.7848,	0.6925,	0.5894,	88.95,	0.7223,	1,	1.0960],
              [0.7158,	0.6317,	0.5376,	81.15,	0.6588,	0.9123,	1]]

print(arbitrage(curr_rates))
