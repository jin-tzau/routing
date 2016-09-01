#-*- coding: utf-8 -*-

import unittest
import networkx as nx
import math

def get_shortest_path(G, s, t):
    return dijkstra(G, s, t)


def dijkstra(G, s, t):
    '''reference: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
    '''
    def get_nodes(G):
        return list(G.node.keys())

    def distance(s, v, G=None):
        return G[s][v]['weight']

    
    Q = get_nodes(G)
    dist = {k: float("inf") for k in get_nodes(G)}
    prev = {k: None for k in get_nodes(G)}
    dist[s] = 0

    while len(Q) > 0:
        unvisited_dist = {k:v for k,v in dist.items() if k in Q}
        u = min(unvisited_dist, key=lambda k: unvisited_dist[k])
        Q.remove(u)

        for v in G.neighbors_iter(u):
            alt = dist[u] + distance(u, v, G)
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    # build spf
    S = []
    u = t
    while prev[u]:
        S.append(u)
        u = prev[u]
    else:
        S.append(u)

    return list(reversed(S))


class TestSPF(unittest.TestCase):
    def setUp(self):
        edges = [
            ("A", "B", {'weight': 1}),
            ("A", "C", {'weight': 10}),
            ("A", "D", {'weight': 10}),
            ("B", "C", {'weight': 1}),
            ("B", "F", {'weight': 10}),
            ("C", "D", {'weight': 10}),
            ("C", "E", {'weight': 1}),
            ("D", "E", {'weight': 10}),
        ]
        self.G = nx.Graph()
        self.G.add_edges_from(edges)

    def test_get_shortest_path(self):
        self.assertEqual(get_shortest_path(self.G, "A", "E"),
                         ['A', 'B', 'C', 'E'])


if __name__=='__main__':
    unittest.main()
