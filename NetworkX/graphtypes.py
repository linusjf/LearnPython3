#!/usr/bin/env python
# -*- coding: utf-8 -*-
import networkx as nx


def printgraph(G):
    print(G)
    print("Nodes: ", G.nodes(data=True))
    print("Edges: ", G.edges(data=True))


# Create an empty graph structure (a “null graph”) with no nodes and no edges.
G = nx.Graph()
# G can be grown in several ways.
# Nodes:
# Add one node at a time:
G.add_node(1)
printgraph(G)
# Add the nodes from any container (a list, dict, set or even the lines from a file or the nodes from another graph).
G.add_nodes_from([2, 3])
printgraph(G)
G.add_nodes_from(range(100, 110))
printgraph(G)
H = nx.path_graph(10)
printgraph(H)
G.add_nodes_from(H)
# In addition to strings and integers any hashable Python object (except None) can represent a node, e.g. a customized
# node object, or even another Graph.
G.add_node(H)
printgraph(G)
# Edges:
# G can also be grown by adding edges.
# Add one edge,
G.add_edge(1, 2)
printgraph(G)
# a list of edges,
G.add_edges_from([(1, 2), (1, 3)])
printgraph(G)
# or a collection of edges,
G.add_edges_from(H.edges)
printgraph(G)
# If some edges connect nodes not yet in the graph, the nodes are added automatically. There are no errors when
# adding nodes or edges that already exist.
G = nx.Graph(day="Friday")
print(G.graph)
# Add node attributes using add_node(), add_nodes_from() or G.nodes
G.add_node(1, time="5pm")
printgraph(G)
G.add_nodes_from([3], time="2pm")
print(G.nodes[1])
# node must exist already to use G.nodes
G.nodes[1]["room"] = 714
printgraph(G)
# remove attribute
del G.nodes[1]["room"]
print(list(G.nodes(data=True)))
# edge attributes using add_edge(), add_edges_from(), subscript notation, or G.edges.
G.add_edge(1, 2, weight=4.7)
printgraph(G)
G.add_edges_from([(3, 4), (4, 5)], color="red")
printgraph(G)
G.add_edges_from([(1, 2, {"color": "blue"}), (2, 3, {"weight": 8})])
printgraph(G)
G[1][2]["weight"] = 4.7
printgraph(G)
G.edges[1, 2]["weight"] = 4
printgraph(G)
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


class ThinGraph(nx.Graph):
    all_edge_dict = {"weight": 1}

    def single_edge_dict(self):
        return self.all_edge_dict

    edge_attr_dict_factory = single_edge_dict


G = ThinGraph()
G.add_edge(2, 1)
print(G[2][1])
G.add_edge(2, 2)
print(G[2][2])
print(G[2][1] is G[2][2])

# or DiGraph, MultiGraph, MultiDiGraph, etc
G = nx.Graph()
printgraph(G)
G = nx.Graph(name="my graph")
printgraph(G)
e = [(1, 2), (2, 3), (3, 4)]  # list of edges
G = nx.Graph(e)
printgraph(G)
# Arbitrary graph attribute pairs (key=value) may be assigned
G = nx.Graph(e, day="Friday")
printgraph(G)
print(G.graph)

# or DiGraph, MultiGraph, MultiDiGraph, etc
G = nx.Graph()
G.add_node(1)
printgraph(G)
G.add_node("Hello")
printgraph(G)
K3 = nx.Graph([(0, 1), (1, 2), (2, 0)])
G.add_node(K3)
printgraph(G)
print(G.graph)
print(G.number_of_nodes())
# Use keywords set/change node attributes:
G.add_node(1, size=10)
printgraph(G)
G.add_node(3, weight=0.4, UTM=("13S", 382871, 3972649))
printgraph(G)

# or DiGraph, MultiGraph, MultiDiGraph, etc
G = nx.Graph()
G.add_nodes_from("Hello")
printgraph(G)
K3 = nx.Graph([(0, 1), (1, 2), (2, 0)])
G.add_nodes_from(K3)
printgraph(G)
print(sorted(G.nodes(), key=str))
# Use keywords to update specific node attributes for every node.
G.add_nodes_from([1, 2], size=10)
printgraph(G)
G.add_nodes_from([3, 4], weight=0.4)
printgraph(G)
# Use (node, attrdict) tuples to update attributes for specific nodes.
G.add_nodes_from([(1, dict(size=11)), (2, {"color": "blue"})])
printgraph(G)
G.nodes[1]["size"]
printgraph(G)

H = nx.Graph()
H.add_nodes_from(G.nodes(data=True))
printgraph(H)
print(H.nodes[1]["size"])

# or DiGraph, MultiGraph, MultiDiGraph, etc
G = nx.path_graph(3)
print(list(G.edges))
G.remove_node(1)
print(list(G.edges))
G = nx.path_graph(4)
print(list(G.edges))
G.remove_node(1)
print(list(G.edges))

# or DiGraph, MultiGraph, MultiDiGraph, etc
G = nx.path_graph(3)
e = list(G.nodes)
print(e)
G.remove_nodes_from(e)
print(list(G.nodes))

# or DiGraph, MultiGraph, MultiDiGraph, etc
G = nx.Graph()
e = (1, 2)
# explicit two-node form
G.add_edge(1, 2)
printgraph(G)
# single edge as tuple of two nodes
G.add_edge(*e)
printgraph(G)
# add edges from iterable container
G.add_edges_from([(1, 2)])
printgraph(G)
G.add_edges_from([(3, 4)])
printgraph(G)

G.add_edge(1, 2, weight=3)
G.add_edge(1, 3, weight=7, capacity=15, length=342.7)
printgraph(G)
# For non-string attribute keys, use subscript notation.
G.add_edge(1, 2)
printgraph(G)
G[1][2].update({0: 5})
printgraph(G)
G.edges[1, 2].update({0: 5})
printgraph(G)

# or DiGraph, MultiGraph, MultiDiGraph, etc
G = nx.Graph()
G.add_edges_from([(0, 1), (1, 2)])  # using a list of edge tuples
printgraph(G)
e = zip(range(0, 3), range(1, 4))
# Add the path graph 0-1-2-3
G.add_edges_from(e)
printgraph(G)
# Associate data to edges
G.add_edges_from([(1, 2), (2, 3)], weight=3)
printgraph(G)
G.add_edges_from([(3, 4), (1, 4)], label="WN2898")
printgraph(G)
# or DiGraph, MultiGraph, MultiDiGraph, etc
G = nx.Graph()
G.add_weighted_edges_from([(0, 1, 3.0), (1, 2, 7.5)])
printgraph(G)

# or DiGraph, etc
G = nx.path_graph(4)
printgraph(G)
G.remove_edge(0, 1)
printgraph(G)
e = (1, 2)
# unpacks e from an edge tuple
G.remove_edge(*e)
printgraph(G)
# an edge with attribute data
e = (2, 3, {"weight": 7})
# select first part of edge tuple
G.remove_edge(*e[:2])
printgraph(G)

# or DiGraph, MultiGraph, MultiDiGraph, etc
G = nx.path_graph(4)
printgraph(G)
ebunch = [(1, 2), (2, 3)]
G.remove_edges_from(ebunch)
printgraph(G)

# dict-of-set/list/tuple
adj = {1: {2, 3}, 2: {1, 3}, 3: {1, 2}}
e = [(u, v) for u, nbrs in adj.items() for v in nbrs]
G.update(edges=e, nodes=adj)
printgraph(G)
DG = nx.DiGraph()
printgraph(DG)
# dict-of-dict-of-attribute
adj = {1: {2: 1.3, 3: 0.7}, 2: {1: 1.4}, 3: {1: 0.7}}
e = [(u, v, {"weight": d}) for u, nbrs in adj.items() for v, d in nbrs.items()]
DG.update(edges=e, nodes=adj)
printgraph(DG)
# dict-of-dict-of-dict
adj = {1: {2: {"weight": 1.3}, 3: {"color": 0.7, "weight": 1.2}}}
e = [(u, v, {"weight": d}) for u, nbrs in adj.items() for v, d in nbrs.items()]
DG.update(edges=e, nodes=adj)
printgraph(DG)
# predecessor adjacency (dict-of-set)
pred = {1: {2, 3}, 2: {3}, 3: {3}}
e = [(v, u) for u, nbrs in pred.items() for v in nbrs]
print(e)

# MultiGraph dict-of-dict-of-dict-of-attribute
MDG = nx.MultiDiGraph()
adj = {
    1: {2: {0: {"weight": 1.3}, 1: {"weight": 1.2}}},
    3: {2: {0: {"weight": 0.7}}},
}
e = [
    (u, v, ekey, d)
    for u, nbrs in adj.items()
    for v, keydict in nbrs.items()
    for ekey, d in keydict.items()
]
print(e)
printgraph(MDG)
MDG.update(edges=e)
printgraph(MDG)
G = nx.path_graph(5)
printgraph(G)
G.update(nx.complete_graph(range(4, 10)))
printgraph(G)
from itertools import combinations

edges = ((u, v, {"power": u * v}) for u, v in combinations(range(10, 20), 2) if u * v < 225)
print(edges)
# for singleton, use a container
nodes = [1000]
G.update(edges, nodes)
printgraph(G)

# or DiGraph, MultiGraph, MultiDiGraph, etc
G = nx.path_graph(4)
printgraph(G)
G.clear()
printgraph(G)

# or DiGraph, MultiGraph, MultiDiGraph, etc
G = nx.path_graph(4)
printgraph(G)
G.clear_edges()
printgraph(G)

G = nx.path_graph(3)
printgraph(G)
G.add_node(1, time="5pm")
G.nodes[0]["foo"] = "bar"
print(list(G.nodes(data=True)))
print(list(G.nodes.data()))
print(list(G.nodes(data="foo")))
print(list(G.nodes.data("foo")))
print(list(G.nodes(data="time")))
print(list(G.nodes.data("time")))
print(list(G.nodes(data="time", default="Not Available")))
print(list(G.nodes.data("time", default="Not Available")))

G = nx.Graph()
G.add_node(0)
printgraph(G)
G.add_node(1, weight=2)
printgraph(G)
G.add_node(2, weight=3)
printgraph(G)
print(dict(G.nodes(data="weight", default=1)))

# or DiGraph, MultiGraph, MultiDiGraph, etc
G = nx.path_graph(4)
print([n for n in G])
print(list(G))
# or DiGraph, MultiGraph, MultiDiGraph, etc
G = nx.path_graph(3)
print(G.has_node(0))
print(0 in G)

# or DiGraph, MultiGraph, MultiDiGraph, etc
G = nx.path_graph(4)
print(1 in G)

# or MultiGraph, etc
G = nx.path_graph(3)
G.add_edge(2, 3, weight=5)
print([e for e in G.edges])
# default data is {} (empty dict)
print(G.edges.data())
print(G.edges.data("weight", default=1))
# only edges from these nodes
print(G.edges([0, 3]))
# only edges from node 0
print(G.edges(0))

# or DiGraph, MultiGraph, MultiDiGraph, etc
G = nx.path_graph(4)
# using two nodes
print(G.has_edge(0, 1))
e = (0, 1)
# e is a 2-tuple (u, v)
print(G.has_edge(*e))
e = (0, 1, {"weight": 7})
# e is a 3-tuple (u, v, data_dictionary)
print(G.has_edge(*e[:2]))
# though this gives KeyError if 0 not in G
print(1 in G[0])

# or DiGraph, MultiGraph, MultiDiGraph, etc
G = nx.path_graph(4)
print(G[0][1])
G[0][1]["weight"] = 7
print(G[0][1]["weight"])
print(G[1][0]["weight"])
# or DiGraph, MultiGraph, MultiDiGraph, etc
G = nx.path_graph(4)
# default edge data is {}
print(G.get_edge_data(0, 1))
e = (0, 1)
# tuple form
print(G.get_edge_data(*e))
# edge not in graph, return 0
print(G.get_edge_data("a", "b", default=0))
# or DiGraph, MultiGraph, MultiDiGraph, etc
G = nx.Graph()
G.add_edge("a", "b", weight=7)
print(G["a"])
G = nx.path_graph(4)
print([n for n in G[0]])
# or DiGraph, MultiGraph, MultiDiGraph, etc
G = nx.path_graph(4)
print([n for n in G.neighbors(0)])
