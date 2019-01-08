"""
File name: graphGenerator.py
Author: Mihai Jianu, Daniele La Prova, Lorenzo Mei 
Python version: 3.x
Generatore di Grafi con nodi randomici, di grandezza e range a scelta, ciclico e non.
"""

from Graph.graph.Graph_AdjacencyMatrix import *
from random import randint

def gGenerator(n, rangeG, Cycle = False, debug = False):
    """
    @param n: int
    @param range: int
    @param Ciclo: Bool
    @return Graph
    n = numero di nodi
    rangeG = range di numeri casuali, per creare i nodi
    Ciclo = Se si desidera o meno un grafo con il ciclo
    """
    graph = GraphAdjacencyMatrix()
    if Cycle:
        if debug:
            print("e' un ciclo")
        nIterations = n
    else:
        nIterations = n - 1
    for i in range(0, n ):
        graph.addNode(randint(0, rangeG))
    tailList = graph.getNodes()
    headList = tailList.copy()
    for j in range(0, nIterations):
        if debug:
            print("Start")
            for i in range(0, len(tailList)):
                print(tailList[i].id)
            print ("end")
        tailIndex = randint(0, len(tailList) - 1)
        tailNode = tailList.pop(tailIndex)
        if debug:
            print("Start dopo Pop")
            for i in range(0, len(tailList)):
                print(tailList[i].id)
            print("end dopo pop")
                #print(tailNode.id)
        if Cycle:
            headList.remove(tailNode)
            headIndex = randint(0, len(headList)-1)
            headNode = headList[headIndex]
            headList.insert(tailIndex,tailNode)
        else:
            headIndex = randint(0, len(tailList) - 1)
            headNode = tailList[headIndex]
        graph.insertEdge(tailNode.id, headNode.id, 1)
        graph.insertEdge(headNode.id, tailNode.id, 1)
        if debug:
            edge = graph.getEdge(tailNode.id,headNode.id)
            print(f"edge is {edge.tail}, {edge.head}")
    if debug:
        graph.print()
    return graph