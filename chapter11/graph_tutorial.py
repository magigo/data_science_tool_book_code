# ! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
for e in [(1, 2), (1, 3), (1, 4), (2, 3), (3, 4), (5, 4), (7, 4)]:
    G.add_edge(*e)

print(G.number_of_edges())

nx.draw(G)
plt.show()
pr = nx.pagerank(G, alpha=0.9)
print(pr)

print(G.number_of_nodes())
print(G.number_of_edges())
print(G.nodes())
print(G.edges())
print(G.neighbors(1))


G.remove_node(7)
print(G.edges())
G.remove_edge(1, 3)
print(G.edges())


G.graph['day'] = 'Monday'
print(G.graph)
G.node[1]['name'] = 'jilu'
print(G.nodes(data=True))

G.add_edge(7, 8, weight=4.7)
G.add_edges_from([(3, 8), (4, 5)], color='red')
G.add_edges_from([(9, 1, {'color': 'blue'}), (8, 3, {'weight': 8})])
G[1][2]['weight'] = 4.7
G.edge[1][2]['weight'] = 4
print(G.edges(data=True))
print(G.degree(1))


DG = nx.DiGraph()
DG.add_weighted_edges_from([(1, 2, 0.5), (3, 1, 0.75)])
print(DG.degree(1))
print(DG.out_degree(1))
print(DG.in_degree(1))

tet = nx.tetrahedral_graph()
nx.draw(tet)
plt.show()


# nx.write_edgelist(G, "graph_edges")
G1 = nx.read_edgelist("graph_edges")
print(G1.edges())

#
# nx.subgraph(G, nbunch)      #- induce subgraph of G on nodes in nbunch
# nx.union(G1,G2)             #- graph union
# nx.disjoint_union(G1,G2)    #- graph union assuming all nodes are different
# nx.cartesian_product(G1,G2) #- return Cartesian product graph
# nx.compose(G1,G2)           #- combine graphs identifying nodes common to both
# nx.complement(G)            #- graph complement
# nx.create_empty_copy(G)     #- return an empty copy of the same graph class
# nx.convert_to_undirected(G) #- return an undirected representation of G
# nx.convert_to_directed(G)   #- return a directed representation of G

SG1 = nx.subgraph(G, [1, 2, 3])
SG2 = nx.subgraph(G, [4, 5, 7])
print(SG1.edges())
print(SG2.edges())
print(nx.union(SG1, SG2).edges())

if __name__ == '__main__':
    pass
