"""
File name: HCDFS_module.py
Author: Daniele La Prova, Lorenzo Mei, Mihai Jianu
Python version: 3.x

Modulo contenente la definizione di hasCycleDFS e delle sue funzioni ausiliarie. Tale modulo è progettato per lavorare su grafi rappresentati come matrici di adiacienza.
"""

from Graph.graph.Graph_AdjacencyMatrix import *
from Graph.graph.Graph import *

def hasCycleDFS(G):
    """
    @param G: Graph
    @return: boolean

    Verifica se nel grafo G è presente almeno un ciclo, sfruttando la visita DFS.
    """

    detected = False
    nodeList = G.getNodes()

    if(G.dfs(nodeList[0].id)):
        return "Cycle Detected"

    return "Cycle not detected"