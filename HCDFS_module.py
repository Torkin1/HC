"""
File name: HCDFS_module.py
Author: Daniele La Prova, Lorenzo Mei, Mihai Jianu
Python version: 3.x

Modulo contenente la definizione di hasCycleDFS e delle sue funzioni ausiliarie. Tale modulo è progettato per lavorare su grafi rappresentati come matrici di adiacienza.
"""

from graph.graph.Graph_AdjacencyMatrix import *

def hasCycleDFS(G):
    """
	@param G: Graph
    @return: boolean
    
    Verifica se nel grafo G è presente almeno un ciclo, sfruttando la visita DFS.
    """

    detected = False                           #variabile booleana che tiene conto se è presente un ciclo o no
    nodeList = getNodes()                      #lista dei nodi

	if(dfsCycleDetected(nodeList[0].id)):      #se la chiamata a dfsCycleDetected restituisce 1 allora è presente un ciclo, partiamo dal primo nodo nella lista dei nodi
        detected = True                        #presenza del ciclo

	return detected                        


def dfsCycleDetected(self, rootId):
    """
    Execute a Depth-First Search (DFS) in the graph starting from the
    specified node.
    :param rootId: the root node ID (integer).
    :return: the DFS list of nodes.
    """

    # Utilizzo e modifica della funzione dfs() in Graph.py

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

            ##start modify dfs

            else:                   #se il nodo corrente è in explored allora abbiamo trovato un ciclo
                return 1            

            ##end modify
                
        dfs_nodes.append(node)

    return dfs_nodes



	