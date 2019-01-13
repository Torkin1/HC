"""
File name: graphGenerator.py
Author: Mihai Jianu, Daniele La Prova, Lorenzo Mei 
Python version: 3.x

Modulo contenente la definizione del generatore di Grafi con nodi randomici, di grandezza
e range a scelta, ciclici e non.
"""

from time import time
from Graph.graph.Graph_AdjacencyMatrix import *
from random import randint

MAXNODES = 10000

def gGenerator(n, rangeG, cycle = 0, debug = False):
    """
    @param n: int
    @param rangeG: int
    @param cycle: int, if >0 aggiunge cycle cicli
    @param debug: bool, if True shows execution details
    @return Graph
    
    Genera un grafo con n nodi dal valore intero casuale < rangeG e almeno n - 1 archi
    secondo il seguente algoritmo.

    Per n - 1 volte, esegue un pop di un nodo tail casuale da una tailList composta
    inizialmente da n nodi. Inoltre, sceglie un altro nodo head casuale dalla tailList
    (senza eseguire il pop) e inserisce nel grafo gli archi (tail, head) e (head, tail).
    In questo modo si ottiene un grafo non orientato connesso con n nodi e 2n - 2 archi.
    Se cycle > 0, aggiunge cycle archi al grafo tra nodi non adiacienti tra loro, 
    inserendo dunque cycle cicli. 
    """
    # si assicura che n < MAXNODES per impedire di generare grafi troppo grandi (e dunque ingestibili dal punto di vista dell'occupazione della memoria)
    
    try:
        assert n <= MAXNODES 
    
    except AssertionError:    
        print(f"n = {n} is too big, executing with n = {MAXNODES} instead (see documentation for details) ...)")
        n = MAXNODES

    if debug:
        start = time()

    # inizializza il grafo, aggiungendo n nodi di valore numerico intero casuale.
    
    graph = GraphAdjacencyMatrix()
    for i in range(0, n ):
        graph.addNode(randint(0, rangeG))

    # rende il grafo connesso, senza creare cicli.
    
    nodeList = graph.getNodes()
    tailList = nodeList.copy()
    headList = tailList.copy()

    nIterations = n - 1
    
    for j in range(0, nIterations):
        
        if debug:
            print("start tailList")
            for i in range(0, len(tailList)):
                print(tailList[i].id)
            print ("end tailList")
        
        tailIndex = randint(0, len(tailList) - 1)
        tailNode = tailList.pop(tailIndex)
        
        if debug:
            print("start tailList (after pop)")
            for i in range(0, len(tailList)):
                print(tailList[i].id)
            print("end taiList (after pop)")
            
        headIndex = randint(0, len(tailList) - 1)
        headNode = tailList[headIndex]
        
        graph.insertEdge(tailNode.id, headNode.id, 1)
        graph.insertEdge(headNode.id, tailNode.id, 1)
        
        if debug:
            edge = graph.getEdge(tailNode.id,headNode.id)
            print(f"added edge ({edge.tail}, {edge.head})")
    
    # infine, aggiunge eventualmente il numero di cicli richiesti.

    if cycle > 0:
        
        if debug:
            print(f"attempting to insert {cycle} cycles ...")
        
        for times in range(0, cycle):
            randNode = nodeList[randint(0, n - 1)]
            done = False            
            x = 0
            while x < len(nodeList) and not done:
                if not graph.isAdj(randNode.id, nodeList[x].id) and randNode.id != nodeList[x].id:
                    graph.insertEdge(randNode.id, nodeList[x].id, 1)
                    graph.insertEdge(nodeList[x].id, randNode.id, 1)
                    if debug:
                        print(f"added edge ({randNode.id}, {nodeList[x].id})")
                    done = True
                x += 1

    if debug:
        graph.print()
        print(f"elapsed time is {time() - start} ")
    
    return graph
