#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021  <@localhost>
#
# Distributed under terms of the MIT license.

from math import log


def arbitrage(graph):
    transformed_graph = [[-log(edge) for edge in row] for row in graph]

    # Pick any source vertex -- we can run Bellman-Ford from any vertex and
    # get the right result
    n = len(transformed_graph)
    min_dist = [float("inf")] * n

    min_dist[0] = 0

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


curr_rates = [
    [1, 0.8825, 0.7510, 113.37, 0.9204, 1.2743, 1.3970],
    [1.1331, 1, 0.8510, 128.47, 1.0429, 1.4439, 1.5830],
    [1.3314, 1.1751, 1, 150.94, 1.2255, 1.6966, 1.8601],
    [0.882050, 0.77845, 0.00663, 1, 0.8118, 0.01124, 0.01232],
    [1.0865, 0.9588, 0.8160, 123.18, 1, 1.3845, 1.5178],
    [0.7848, 0.6925, 0.5894, 88.95, 0.7223, 1, 1.0960],
    [0.7158, 0.6317, 0.5376, 81.15, 0.6588, 0.9123, 1],
]

print(arbitrage(curr_rates))

world = [
    [1, 1.1336, 0.0088, 1.3329],
    [0.8821, 1, 0.0078, 1.1758],
    [113.5900, 128.7656, 1, 151.4041],
    [0.7502, 0.8505, 0.0066, 1],
]
print(arbitrage(world))

americas = [
    [1, 0.2460, 0.0469, 0.1779],
    [4.0654, 1, 0.1908, 0.7230],
    [21.3046, 5.2405, 1, 3.7890],
    [5.6227, 1.3831, 0.2639, 1],
]
print(arbitrage(americas))

emea = [
    [1, 1.1336, 1.3330, 1.0866],
    [0.8821, 1, 1.1759, 0.9585],
    [0.7502, 0.8504, 1, 0.8152],
    [0.9203, 1.0433, 1.2268, 1],
]
print(arbitrage(emea))

apac = [
    [1, 0.1571, 0.0088, 0.1283],
    [6.3650, 1, 0.0561, 0.8164],
    [113.5500, 17.8397, 1, 14.5652],
    [7.7960, 1.2248, 0.0687, 1],
]
print(arbitrage(apac))
