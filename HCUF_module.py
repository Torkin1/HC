"""
File name: HCUF_module.py
Author: Mihai Jianu, Daniele La Prova, Lorenzo Mei
Python version: 3.x

Modulo contenente la definizione di hasCycleUF e delle sue funzioni e classi
ausiliarie.
Tale modulo è progettato per lavorare su grafi rappresentati come matrici di 
adiacienza.
"""

from unionFind.quickFind import *
#from unionFind.quickUnion import *
from Graph.graph.Graph_AdjacencyMatrix import *
from D_module import *

class CustomQFB(QuickFindBalanced):
    """
    Versione custom della QFB, implementa il metodo findNode.
    """

    def findNode(self, e):
        """
        @param e: valore dell'elemento cercato
        @return UFB node, None if not found

        Dato un elemento come input, restituisce il nodo che lo contiene tra tutti
        i nodi presenti nella struttura unionFind.
        Se l'elemento passato proviene da un nodo di un grafo si evitano ambiguità,
        dato che ogni nodo possiede un ID unico.
        
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

def edgeGenerator(G, maxTail, maxHead):
    """
    @param G: Graph (as adjacency matrix)
    @param maxTail: int, maximum range of sources
    @param maxHead: int, maximum range of destinations
    @return iterable
    
    Genera un iterabile che scorre gli archi di G t.c. tail, head <= maxTail, maxHead
    """
    
    for src in range(maxTail):
            for dst in range(maxHead):
                if G.adj[src][dst] is not None and G.adj[src][dst] != GraphAdjacencyMatrix.EMPTY and src != dst:
                    yield Edge(src, dst, G.adj[src][dst])

@profiler
def hasCycleUF(G, debug=False, showProfile = False, pathLog = "log.txt"):
    """
    @param G: Graph (as adjacency matrix)
    @return bool

    Verifica se nel grafo G è presente almeno un ciclo, sfruttando la struttura dati
    UnionFind e un iterator per scandirne tutti gli archi.

    procedure hasCycleUF(Graph G) → bool
        uf ← UnionFind
        for all unvisited (u, v) ∈ E(G) do
            if uf.find(u) == uf.find(v) then cycle detected
            else uf.union(u, v)
        return no cycle present

    """ 
    
    uf = CustomQFB()
    edges = edgeGenerator(G, len(G.adj), len(G.adj))
    countEdge = 0

    while True:
        try:
            currentEdge = next(edges)
            countEdge += 1
            if debug == True:
                print(f"current edge is {currentEdge}")

            # se gli elementi non appartengono a nessun nodo, vengono creati nuovi set con tali elementi all'interno (uno per elemento)

            if uf.findNode(currentEdge.tail) == None:
                uf.makeSet(currentEdge.tail)

            if uf.findNode(currentEdge.head) == None:    
                uf.makeSet(currentEdge.head)

            if debug == True:
                uf.print()

            # trova il nodo nella uf contenente tali elementi
            
            tailNode, headNode = uf.findNode(currentEdge.tail), uf.findNode(currentEdge.head)   
            if debug == True:
                print(f"tailNode is {tailNode}, headNode is {headNode}")
                        
            # genera gli archi finora esplorati e controlla se currentEdge sia già presente o meno tra di essi, per evitare che venga esplorato nell'altro senso (e dunque avere l'illusione di un ciclo)
            
            edgeSeen = edgeGenerator(G, len(G.adj), len(G.adj))
            if debug:
                print("controllo se ho già percorso l'arco ...")

            exit, seen = False, False
            while not exit :
                try:
                    currentSeen = next(edgeSeen)
                    if debug:
                        print(f"currentSeen is {currentSeen}")
                    if currentEdge.tail == currentSeen.tail and currentEdge.head == currentSeen.head:
                        raise StopIteration
                    
                    if currentEdge.tail == currentSeen.head and currentEdge.head == currentSeen.tail: #and countSeen < countEdge:
                        
                        if debug:
                            print("già percorso")

                        seen = True
                        raise StopIteration

                except StopIteration:
                        if debug:
                            print(f"seen edges terminated ...")
                        exit = True

            # controlla se c'è un ciclo, altrimenti continua
            
            if uf.find(tailNode) == uf.find(headNode) and not seen:
                return True
            else:
                uf.union(uf.findRoot(tailNode), uf.findRoot(headNode))
                
                if debug == True:
                    uf.print()
                
        except StopIteration:
            if debug == True:
                print("iteration terminated, exiting ...")
            return False                    
