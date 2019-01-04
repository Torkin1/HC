"""
    File name: unionFind.py
    Author: Ovidiu Daniel Barba
    Date created: 7/12/2018
    Date last modified: 7/12/2018
    Python Version: 3.7

    Modulo che contiene gli elemeti di base per definire
    la struttura dati Union-Find
"""


class UFNode:
    """
    Nodo semplice di una struttura dati union-find.
    """
    def __init__(self, e):
        self.elem = e
        self.father = None
        self.sons = []

    def __str__(self):
        return f"{self.elem}"

    def __repr__(self):
        return self.__str__()


class UFBalancedNode(UFNode):
    """
    Nodo di una struttura dati union-find che
    contiene anche la size del sottoalbero
    radicato nel nodo. Utile nelle varie UnionFind
    bilanciate
    """
    def __init__(self, e):
        super().__init__(e)
        self.size = 1


class UnionFind:
    """
    Classe con i metodi base dell'Union-Find
    """
    def makeSet(self, e):
        """
        Crea un nuovo insieme {e} con un nuovo elemento e.
        Il nome dell'insieme è e
        :param e:
        """
        pass

    def union(self, a, b):
        """
        Fonde i due insiemi a e b in un unico insieme.
        Il nome dell'insieme ottenuto è a. Questa operazione
        distrugge i vecchi insiemi a e b
        :param a: primo insieme
        :param b: secondo insieme
        """
        pass

    def find(self, e):
        """
        Restituisce il nome dell'insieme che contiene
        l'elemento e
        :param e: elemento
        :return: nome insieme contenente e
        """
        pass

    def findRoot(self, node):
        """
        Restituisce il nodo radice dell'insieme, il
        quale contiene il nome dell'insieme
        :param node:
        :return: radice dell'insieme
        """
        pass
