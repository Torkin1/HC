"""
File name: graphGenerator.py
Author: Mihai Jianu, Daniele La Prova, Lorenzo Mei 
Python version: 3.x

Generatore di Grafi con nodi randomici, di grandezza e range a scelta, ciclico e non.
"""

from Graph.graph.Graph_AdjacencyMatrix import *
from random import randint

def gGenerator(n, rangeG, Ciclo = False):
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
                if j != k:  # Altrimenti, inserisce archi con tail == head  -Daniele    
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


def createGenericGraph(n, rangeG, Cycle = False):

        graph = GraphAdjacencyMatrix()
        idList = []
        nodeCount = 0
        serviceNodes = 2*(n - 1)
        #count = 1

        #create all nodes
        for i in range(0, n):
            graph.addNode(randint(0, rangeG))
            idList.append(i)
        
        if Cycle:
            
            while(nodeCount < n):
                nodeDst = idList[randint(0, len(idList) - 1)]

                print(nodeCount)
                
                if nodeCount != nodeDst :
                    print(nodeDst)
                    print(idList)

                    graph.insertEdge(nodeCount, nodeDst, 1)
                    graph.insertEdge(nodeDst, nodeCount, 1)
                    nodeCount += 1

        ####    IN COSTRUZIONE  ####

        else:
            while(nodeCount < n - 1 or graph.numEdges() < 2*(n - 1)):
                nodeDst = idList[randint(0, len(idList) - 1)]

                print(nodeCount)
                
                if nodeCount != nodeDst:
                    print(nodeDst)
                    print(idList)

                    graph.insertEdge(nodeCount, nodeDst, 1)
                    graph.insertEdge(nodeDst, nodeCount, 1)
                    nodeCount += 1

                

        #graph.print()

        #check if the graph is connected
        #i = 0

        #while(i < n and count != 0):
            
            #if len(graph.getAdj(i)) < 2:
                #print("not connected")
                #nodeDest = randint(0, n - 1)

                #if nodeDest != i:
                    #print("Insert edge {}, {}".format(i, nodeDest))
                    #graph.insertEdge(i, nodeDest, 1)
                    #graph.insertEdge(nodeDest, i, 1)
                    #i += 1
                    #count -= 1

            #else:
                #i += 1

        graph.print()
        return graph