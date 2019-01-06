"""
File name: HCDFS_module.py
Author: Daniele La Prova, Lorenzo Mei, Mihai Jianu
Python version: 3.x

Modulo contenente la definizione di hasCycleDFS e delle sue funzioni ausiliarie. Tale modulo è progettato per lavorare su grafi rappresentati come matrici di adiacienza.
"""

from Decorator_module import *
from Graph.graph.Graph_AdjacencyMatrix import *
from Graph.graph.Graph import *


class subGraphBase(GraphAdjacencyMatrix):

    def __init__(self, G):
        """
        Constructor.
        """

        super().__init__()

        self.nodes = G.nodes
        self.nextId = G.nextId
        self.adj = G.adj


    def dfsDetectedCycle(self, rootId):
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

                if adj_node not in explored:
                    s.push(adj_node)

                elif len(dfs_nodes) > 0 and adj_node != dfs_nodes[-1]:
                    return True

            dfs_nodes.append(node)

        return False

@profiler
def hasCycleDFS(G):
    """
    @param G: Graph
    @return: boolean

    Verifica se nel grafo G è presente almeno un ciclo, sfruttando la visita DFS.
    """
    graph = subGraphBase(G)
    nodeList = graph.getNodes()

    if graph.dfsDetectedCycle(nodeList[0].id):
        return True

    return False
