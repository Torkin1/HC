"""
File name: graphGenerator.py
Author: Mihai Jianu, Daniele La Prova, Lorenzo Mei 
Python version: 3.x

Generatore di Grafi con nodi randomici, di grandezza e range a scelta, ciclico e non.
"""

from Graph.graph.Graph_AdjacencyMatrix import *
from random import randint

def gGenerator(n, rangeG, Ciclo = True):
    """
    @param n: int
    @param range: int
    @param Ciclo: Bool
    @return Graph

    n = numero di nodi
    rangeG = range di numeri casuali, per creare i nodi
    Ciclo = Se si desidera o meno un grafo con il ciclo
    """

    if  Ciclo:
        g = GraphAdjacencyMatrix()
        for i in range(0, n):
            g.addNode(randint(0, rangeG))
        for j in range(0, n + 1):
            for k in range(0, n + 1):
                g.insertEdge(j, k, 1)
        g.print()
        return g
    else:
        g = GraphAdjacencyMatrix()
        for i in range(0, n):
            g.addNode(randint(0, rangeG))
        for j in range(0, n):
            g.insertEdge(j, j + 1, 1)
        for k in range(0, n):
            g.insertEdge(k + 1, k, 1)
        g.print()
        return g
