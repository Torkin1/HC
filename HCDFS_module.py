"""
File name: HCDFS_module.py
Author: Daniele La Prova, Lorenzo Mei, Mihai Jianu
Python version: 3.x

Modulo contenente la definizione di hasCycleDFS e delle sue funzioni ausiliarie. Tale modulo è progettato per lavorare su grafi rappresentati come matrici di adiacienza.
"""

from Graph.graph.Graph_AdjacencyMatrix import *
from Graph.graph.Graph import *
from Decorator_module import *


class CustomGAM(GraphAdjacencyMatrix):

    def __init__(self, G):
        """
        Constructor.
        """

        super().__init__()

        self.nodes = G.nodes
        self.nextId = G.nextId
        self.adj = G.adj

    #@profiler
    def dfsDetectedCycle(self, rootId, debug):
        """
        Execute a Depth-First Search (DFS) in the graph starting from the
        specified node and check if a cycle is detected.
        :param rootId: the root node ID (integer).
        :return: boolean
        """
        # if the root does not exists, return None
        if rootId not in self.nodes:
            return None

        # DFS nodes initialization
        dfs_nodes = []

        # queue initialization
        s = Stack()
        s.push(rootId)

        explored = {rootId}  # nodes already explored

        while not s.isEmpty():  # while there are nodes to explore ...
            
            node = s.pop()  # get the node from the stack
            explored.add(node)  # mark the node as explored 

            # add all adjacent unexplored nodes to the stack
            for adj_node in self.getAdj(node):
                countSeen = 0   #contatore delle volte in cui è stato visto adj_node nello stack

                if adj_node not in explored:
                    s.push(adj_node)

                    for elem in s.s:    #conteggio della presenza del nodo nello stack
                        if adj_node == elem:
                            countSeen += 1

                if countSeen > 1:    #Se ho visto almeno 2 volte lo stesso nodo nello stack ho un ciclo 
                    return True

                if debug:
                    print("-------")
                    print(f"Current node: {node}")
                    print(f"Adjacent node: {adj_node}")
                    print(f"Explored nodes: {explored}")
                    print(f"DFS list: {dfs_nodes}")              
                    print("-------")

            dfs_nodes.append(node)

        return False

@profiler
def hasCycleDFS(G, debug = False, showProfile = False, timeAccuracy = False):
    """
    @param G: Graph
    @return: boolean

    Verifica se nel grafo G è presente almeno un ciclo, sfruttando la visita DFS.
    """
    graph = CustomGAM(G)
    nodeList = graph.getNodes()

    if graph.dfsDetectedCycle(nodeList[0].id, debug):   #Facciamo partire la visita DFS dal primo nodo presente in nodeList
        return True

    return False
