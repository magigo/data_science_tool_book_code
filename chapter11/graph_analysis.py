from __future__ import print_function
from networkx import read_edgelist
import networkx as nx

G = read_edgelist('hartford_drug.edgelist')
print(G.number_of_nodes())
print(G.number_of_edges())

import matplotlib.pyplot as plt
nx.draw(G)
plt.show()
