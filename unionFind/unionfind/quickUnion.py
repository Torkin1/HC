"""
    File name: quickUnion.py
    Author: Ovidiu Daniel Barba
    Date created: 7/12/2018
    Date last modified: 7/12/2018
    Python Version: 3.7

    Modulo che contiene l'implementazione base di QuickUnion
    e la versione bilanciata
"""

from unionfind.unionFind import *


class QuickUnion(UnionFind):
    """
    Implementazione della versione QuickUnion base
    che esegue rapidamente l'operazione union O(1) a scapito della find O(n)
    """
    def __init__(self):
        self.nodes = []

    def makeSet(self, e):
        """
        Crea un albero di un solo nodo e lo appende alla lista dei nodi.
        O(1)
        :param e: elemento
        """
        node = UFNode(e)
        self.nodes.append(node)

    def find(self, node):
        """
        Ritorna il nome dell'insieme a cui appartiene node.
        O(n)
        :param node:
        :return:
        """
        return self.findRoot(node).elem

    def union(self, rootA, rootB):
        """
         Appende la radice dell'albero radicato in rootB alla radice rootA dell'altro.
         O(1)
        :param rootA:
        :param rootB:
        """
        if rootA == rootB:
            return
        rootB.father = rootA
        rootA.sons.append(rootB)

    def findRoot(self, node):
        """
        Trova la radice dell'albero a cui appartiene questo nodo
        risalendo di padre in padre. Nel caso peggiore
        dobbiamo attraversare n elementi (numero makeSet)
        O(n)
        :param node:
        :return: radice
        """
        root = node
        while root.father is not None:  # root non e' ancora la radice
            root = root.father
        return root

    def __printFromRoot(self, root):
        print(f"Set with name {root.elem}. Elements: ")
        print(root)  # adesso la radice contiene direttamente l'elemento, diversamente da QuickFind
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


class QuickUnionBalanced(QuickUnion):
    """
    Versione di QuickUnion che migliora la find a O(log n).
    Union by size.
    """
    def makeSet(self, e):
        """
        Crea un albero con un solo nodo
        :param e:
        :return:
        """
        node = UFBalancedNode(e)
        self.nodes.append(node)

    def union(self, rootA, rootB):
        """
        Appende la radice dell'albero con size minore alla radice dell'albero
        con size maggiore
        :param rootA:
        :param rootB:
        """
        if rootA == rootB:
            return
        if rootA.size >= rootB.size:
            rootA.size += rootB.size
            rootB.father = rootA
            rootA.sons.append(rootB)
        else:
            rootB.size += rootA.size
            rootA.father = rootB
            rootB.sons.append(rootA)


class QuickUnionBalancedPathCompression(QuickUnionBalanced):
    """
    Effettua la path compression per migliorare ulteriormente la
    find riducendo l'altezza dell'albero
    """
    # def findRoot(self, node):
    #     relatives = []
    #     root = node
    #     depth = 0
    #     while root.father is not None:
    #         relatives.append(root)  # colleziona tutti i nodi incontrati
    #         root = root.father
    #         depth += 1
    #     if depth >= 3:
    #         for node in relatives[:-1]:  # collega tutti alla radice tranne l'ultimo
    #             node.father = root
    #             root.sons.append(node)
    #     return root

    def findRoot(self, node):
        """
        Funzione ricorsiva che trova la radice partendo dal nodo node.
        Inoltre fa path-compression per ridurre ulteriormente l'altezza
        dell'albero per migliorare le successive find
        :param node:
        :return:
        """
        if node.father is None:
            return node
        else:
            node.father = self.findRoot(node.father)
            return node.father


class QuickUnionBalancedPathSplitting(QuickUnionBalanced):
    """
    Effettua la path splitting per migliorare ulteriormente la
    find riducendo l'altezza dell'albero.
    Rende i nodi dei livelli 3 in giù figli dei propri nonni
    """
    def findRoot(self, node):
        while node.father is not None:
            node, node.father = node.father, node.father.father
        return node

