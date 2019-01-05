"""
File name: HCUF_module.py
Author: Daniele La Prova, Lorenzo Mei, Mihai Jianu
Python version: 3.x

Modulo contenente la definizione di hasCycleUF e delle sue funzioni ausiliarie. Tale modulo è progettato per lavorare su grafi rappresentati come matrici di adiacienza.
"""

from unionFind.quickFind import *
#from unionFind.quickUnion import *
from Graph.graph.Graph_AdjacencyMatrix import *

def edgeGenerator(G):
    """
    @param G: Graph
    @return iterable
    
    Genera un iterabile che scorre gli archi di G.
    """
    # Liberamente ispirato a Graph_AdjacencyMatrix.getEdges()
    
    for src in range(len(self.adj)):
            for dst in range(len(self.adj)):
                if self.adj[src][dst] is not None and self.adj[src][dst] != GraphAdjacencyMatrix.EMPTY:
                    yield Edge(src, dst, self.adj[src][dst])


def hasCycleUF(G):
    """
    @param G: Graph (as adjacency matrix)
    @return bool

    Verifica se nel grafo G è presente almeno un ciclo, sfruttando la struttura dati UnionFind e un iterator per scandirne tutti gli archi.

    procedure hasCycleUF(Graph G) → bool
        uf ← UnionFind
        for all unvisited (u, v) ∈ E(G) do
            if uf.find(u) == uf.find(v) then cycle detected
            else uf.union(u, v)
        return no cycle present

    """ 
    
    #uf = QuickUnionBalanced
    uf = QuickFindBalanced()
    exit = False
    edge = edgeGenerator(G)

    while not exit:
        try:
            currentEdge = next(edge)
            tailSet, headSet = uf.makeSet(currentEdge.tail), uf.makeSet(currentEdge.head)
            if uf.find(tailset) == uf.find(headSet):
                return True
            else:
                uf.union(uf.findRoot(tailSet), uf.findRoot(headSet))
        except StopIteration:
                exit = True
    return False
