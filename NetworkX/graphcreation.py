#!/usr/bin/env python
# -*- coding: utf-8 -*-
import networkx as nx
G = nx.Graph()
# default edge data=1
G.add_edge(1, 2) 
# specify edge data
G.add_edge(2, 3, weight=0.9) 

import math
# any hashable can be a node
G.add_edge('y', 'x', function=math.cos)
G.add_node(math.cos) 
elist = [(1, 2), (2, 3), (1, 4), (4, 2)]
G.add_edges_from(elist)
elist = [('a', 'b', 5.0), ('b', 'c', 3.0), ('a', 'c', 1.0), ('c', 'd', 7.3)]
G.add_weighted_edges_from(elist)
print(G)

G = nx.Graph()
e = [('a', 'b', 0.3), ('b', 'c', 0.9), ('a', 'c', 0.5), ('c', 'd', 1.2)]
G.add_weighted_edges_from(e)
print(nx.dijkstra_path(G, 'a', 'd'))

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('graphcreation.pdf')
print("Setup Complete")
G = nx.cubical_graph()
subax1 = plt.subplot(121)
# default spring_layout
nx.draw(G) 
subax2 = plt.subplot(122)
nx.draw(G, pos=nx.circular_layout(G), node_color='r', edge_color='b')
pp.savefig()
pp.close()

G = nx.Graph()
G.add_edge('A', 'B')
G.add_edge('B', 'C')
print(G.adj)

G = nx.Graph()
G.add_edge(1, 2, color='red', weight=0.84, size=300)
print(G[1][2]['size'])
print(G.edges[1, 2]['color'])
