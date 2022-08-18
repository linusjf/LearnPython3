#!/usr/bin/env python
# -*- coding: utf-8 -*-
import networkx as nx
# Create an empty graph structure (a “null graph”) with no nodes and no edges.
G = nx.Graph()
# G can be grown in several ways.
# Nodes:
# Add one node at a time:
G.add_node(1)
print(G)
# Add the nodes from any container (a list, dict, set or even the lines from a file or the nodes from another graph).
G.add_nodes_from([2, 3])
print(G)
G.add_nodes_from(range(100, 110))
print(G)
H = nx.path_graph(10)
print(H)
G.add_nodes_from(H)
# In addition to strings and integers any hashable Python object (except None) can represent a node, e.g. a customized
# node object, or even another Graph.
G.add_node(H)
print(G)
# Edges:
# G can also be grown by adding edges.
# Add one edge,
G.add_edge(1, 2)
print(G)
# a list of edges,
G.add_edges_from([(1, 2), (1, 3)])
print(G)
# or a collection of edges,
G.add_edges_from(H.edges)
print(G)
# If some edges connect nodes not yet in the graph, the nodes are added automatically. There are no errors when
# adding nodes or edges that already exist.
