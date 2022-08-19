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
G = nx.Graph(day="Friday")
print(G.graph)
# Add node attributes using add_node(), add_nodes_from() or G.nodes
G.add_node(1, time="5pm")
print(G)
G.add_nodes_from([3], time="2pm")
print(G.nodes[1])
# node must exist already to use G.nodes
G.nodes[1]["room"] = 714 
print(G)
# remove attribute
del G.nodes[1]["room"]
print(list(G.nodes(data=True)))
# edge attributes using add_edge(), add_edges_from(), subscript notation, or G.edges.
G.add_edge(1, 2, weight=4.7)
print(G)
G.add_edges_from([(3, 4), (4, 5)], color="red")
print(G)
G.add_edges_from([(1, 2, {"color": "blue"}), (2, 3, {"weight": 8})])
print(G)
G[1][2]["weight"] = 4.7
print(G)
G.edges[1, 2]["weight"] = 4
print(G)
# check if node in graph
print(1 in G)
# iterate through nodes
print([n for n in G if n < 3]) 
# number of nodes in graph
print(len(G)) 

for n, nbrsdict in G.adjacency():
    for nbr, eattr in nbrsdict.items():
        if "weight" in eattr:
            print(eattr)
            pass

for u, v, weight in G.edges.data("weight"):
    if weight is not None:
        # Do something useful with the edges
        print(weight)
        pass
