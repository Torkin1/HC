"""
    File name: quickFind.py
    Author: Ovidiu Daniel Barba
    Date created: 7/12/2018
    Date last modified: 7/12/2018
    Python Version: 3.7

    Modulo che contiene l'implementazione base di QuickFind
    e la versione bilanciata
"""

from unionfind.unionFind import *


class QuickFind(UnionFind):
    """
    Implementazione della versione QuickFind base
    che esegue rapidamente l'operazione find O(1) a scapito della union O(n)
    """
    def __init__(self):
        self.nodes = []  # lista contenente tutti i nodi appartenenti all'insieme

    def makeSet(self, e):
        """
        Crea un nuovo albero di altezza 1.
        L'albero sara' composto dal nodo contenente l'elemento passato come
        parametro piu' un nodo radice avente medesimo nome (il nome dell'insieme)
        O(1)
        :param e: elemento da inserire
        """
        root = UFNode(e)
        node = UFNode(e)
        root.sons.append(node)
        node.father = root
        self.nodes.append(node)

    def union(self, rootA, rootB):
        """
        Sostituisce tutti i puntatori dalle foglie radicate in rootB con
        puntatori alla radice di A (rootA). Infine cancella la vecchia radice
        rootB.
        O(n)
        :param rootA:
        :param rootB:
        """
        if rootA == rootB:  # si vuole fondere lo stesso albero!
            return          # fai niente
        for sonB in rootB.sons:
            rootA.sons.append(sonB)  # sposta tutti i figli di B in A
            sonB.father = rootA

    def find(self, node):
        """
        Restituisce il nome memorizzato nel padre del nodo
        (coincide con la radice) e rappresenta il nome dell'insieme
        contente node
        O(1)
        :param node:
        :return: nome dell'insieme a cui appartiene
        """
        return self.findRoot(node).elem

    def findRoot(self, node):
        """
        Restituisce la radice dell'insieme (in questo caso il padre).
        O(1)
        :param node:
        :return: radice
        """
        return node.father

    def __printFromRoot(self, root):
        print(f"Set with name {root.elem}. Elements: ")
        for son in root.sons:
            print(son)

    def print(self):
        print("----UnionFind---")
        printedRoots = []
        for i in self.nodes:
            root = self.findRoot(i)
            if root not in printedRoots:
                self.__printFromRoot(root)
                printedRoots.append(root)
        print("----End UnionFind----")


class QuickFindBalanced(QuickFind):
    """
    Versione di QuickFind che migliora la union a O(log n)
    """
    def makeSet(self, e):
        """
        Usa gli UFBalancedNode al posto
        degli UFNode
        O(1)
        :param e:
        :return:
        """
        root = UFBalancedNode(e)
        son = UFBalancedNode(e)
        root.sons.append(son)
        son.father = root
        self.nodes.append(son)

    def union(self, rootA, rootB):
        """
        La radice con meno figli cede i propri figli all'altra radice.
        O(log n)
        :param rootA:
        :param rootB:
        """
        if rootA == rootB:
            return rootA

        if rootA.size >= rootB.size:
            for sonB in rootB.sons:
                sonB.father = rootA
                rootA.sons.append(sonB)
            rootA.size += rootB.size
        else:
            for sonA in rootA.sons:
                sonA.father = rootB
                rootB.sons.append(sonA)
            rootB.size += rootA.size
            rootB.elem = rootA.elem  # aggiorniamo il nome di B con quello di A
