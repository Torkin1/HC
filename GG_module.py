"""
File name: graphGenerator.py
Author: Mihai Jianu, Daniele La Prova, Lorenzo Mei 
Python version: 3.x
Generatore di Grafi con nodi randomici, di grandezza e range a scelta, ciclico e non.
"""

from time import time
from Graph.graph.Graph_AdjacencyMatrix import *
from random import randint

def gGenerator(n, rangeG, cycle = 0, debug = False):
    """
    @param n: int
    @param range: int
    @param Ciclo: Bool
    @return Graph
    n = numero di nodi
    rangeG = range di numeri casuali, per creare i nodi
    Ciclo = Se si desidera o meno un grafo con il ciclo
    """
    start = time()

    graph = GraphAdjacencyMatrix()
    
    for i in range(0, n ):
        graph.addNode(randint(0, rangeG))
    nodeList = graph.getNodes()
    tailList = nodeList.copy()
    headList = tailList.copy()
    

    nIterations = n - 1
    
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
            
        headIndex = randint(0, len(tailList) - 1)
        headNode = tailList[headIndex]
        
        graph.insertEdge(tailNode.id, headNode.id, 1)
        graph.insertEdge(headNode.id, tailNode.id, 1)
        
        if debug:
            edge = graph.getEdge(tailNode.id,headNode.id)
            print(f"edge is {edge.tail}, {edge.head}")
    
    if cycle > 0:
        
        if debug:
            print(f"tentativo di inserimento di un ciclo ...")
        
        for times in range(0, cycle):
            randNode = nodeList[randint(0, n - 1)]
            adjList = graph.getAdj(randNode.id)
            done = False
            
            x = 0
            while x < len(nodeList) and not done:
                if not graph.isAdj(randNode.id, nodeList[x].id) and randNode.id != nodeList[x].id:
                    graph.insertEdge(randNode.id, nodeList[x].id, 1)
                    graph.insertEdge(nodeList[x].id, randNode.id, 1)
                    if debug:
                        print(f"edge added is ({randNode.id}, {nodeList[x].id})")
                    done = True
                x += 1

    if debug:
        graph.print()
    
    print(f"elapsed time is {time() - start} ")
    return graph
