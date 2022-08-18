#!/usr/bin/env python
# -*- coding: utf-8 -*-
import networkx as nx
# Create an empty graph structure (a “null graph”) with no nodes and no edges.
G = nx.Graph()
# G can be grown in several ways.
# Nodes:
# Add one node at a time:
G.add_node(1)
# Add the nodes from any container (a list, dict, set or even the lines from a file or the nodes from another graph).
G.add_nodes_from([2, 3])
G.add_nodes_from(range(100, 110))
H = nx.path_graph(10)
print(H)
G.add_nodes_from(H)
# In addition to strings and integers any hashable Python object (except None) can represent a node, e.g. a customized
# node object, or even another Graph.
G.add_node(H)
print(G)
