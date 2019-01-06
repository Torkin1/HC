# WIP: non funge! Ritorna sempre True indipendentemente dal valore di Ciclo.

"""
File name: HCUF_module.py
Author: Daniele La Prova, Lorenzo Mei, Mihai Jianu
Python version: 3.x

Modulo contenente la definizione di hasCycleUF e delle sue funzioni e classi ausiliarie. Tale modulo è progettato per lavorare su grafi rappresentati come matrici di adiacienza.
"""

from unionFind.quickFind import *
#from unionFind.quickUnion import *
from Graph.graph.Graph_AdjacencyMatrix import *

class CustomQFB(QuickFindBalanced):
    """
    Versione custom della QFB, implementa il metodo findNode.
    """

    def findNode(self, e):
        """
        @param e: valore dell'elemento cercato
        @return UFB node

        Dato un elemento come input, restituisce il nodo che lo contiene tra tutti i nodi presenti nella struttura unionFind.
        """
        touchedRoots = []
        for i in self.nodes:
            currentRoot = self.findRoot(i)
            if currentRoot not in touchedRoots:
                for son in currentRoot.sons:
                    if son.elem == e:
                        return son
                touchedRoots.append(currentRoot)
        return None

def edgeGenerator(G):
    """
    @param G: Graph
    @return iterable
    
    Genera un iterabile che scorre gli archi di G.
    """
    # Liberamente ispirato a Graph_AdjacencyMatrix.getEdges()
    
    for src in range(len(G.adj)):
            for dst in range(len(G.adj)):
                if G.adj[src][dst] is not None and G.adj[src][dst] != GraphAdjacencyMatrix.EMPTY and src != dst:
                    yield Edge(src, dst, G.adj[src][dst])


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
    uf = CustomQFB()
    exit = False
    edges = edgeGenerator(G)

    while not exit:
        try:
            currentEdge = next(edges)

            if uf.findNode(currentEdge.tail) == None:
                uf.makeSet(currentEdge.tail)

            if uf.findNode(currentEdge.head) == None:    
                uf.makeSet(currentEdge.head)

            tailNode, headNode = uf.findNode(currentEdge.tail), uf.findNode(currentEdge.head)
            if uf.find(tailNode) == uf.find(headNode):
                return True
            else:
                uf.union(uf.findRoot(tailNode), uf.findRoot(headNode))
        except StopIteration:
                exit = True
    return False
