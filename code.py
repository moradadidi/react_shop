import networkx as nx
import numpy as np

# Example graphs
G = nx.Graph()
G.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4)])

# Random walk with restart (personalized PageRank)
p = nx.pagerank(G, alpha=0.85)

print(f"Random Walk-Based Similarity: {p}")
