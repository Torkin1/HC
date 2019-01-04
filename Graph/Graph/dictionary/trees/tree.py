"""
    File name: tree.py
    Author: Ovidiu Daniel Barba
    Date created: 14/11/2018
    Date last modified: 14/11/2018
    Python Version: 3.7

    Questo modulo contiene la classe Tree che rappresenta
    un generico albero.
    La classe va estesa per creare uno specifico tipo di albero
    (binario, d-ario, AVL, ecc)
"""

class Tree:
    """
    Classe che rappresenta un albero con i principali metodi
    """
    def nodesNumber(self):
        """
        :return: numero di nodi dell'albero
        """
        pass

    def degree(self, node):
        """
        :param node:
        :return: numero di figli di node
        """
        pass

    def fatherOf(self, node):
        """
        :param node:
        :return: padre di node
        """
        pass

    def sonsOf(self, node):
        """
        :param node:
        :return: lista dei figli di node
        """
        pass

    def cut(self, node):
        """
        Sradica l'albero da node (compreso)
        :param node:
        :return:
        """
        pass

    def print(self):
        pass
