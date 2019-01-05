"""
    File name: avlTree.py
    Author: Ovidiu Daniel Barba
    Date created: 14/11/2018
    Date last modified: 14/11/2018
    Python Version: 3.7

    Questo modulo contiene l'implementazione
    dell'albero AVL, un albero binario di ricerca
    bilanciato in altezza
"""

from dictionary.trees.binaryTree import BinaryTree
from dictionary.trees.binaryTree import BinaryNode
from dictionary.dictTrees.binarySearchTree import BinarySearchTree


class AVLTree(BinarySearchTree):
    """
    Un albero AVL è un albero di ricerca binario bilanciato
    in altezza. Dopo inserimenti e cancellazioni, vengono eseguite
    (se necessarie) rotazioni per mantenere il bilanciamento
    """
    HEIGHT_INDEX = 2

    def __init__(self):
        super().__init__()
        # Node's info now is a triple [ key, value, height]
    
    def __height(self, node):
        """
        Restituisce l'altezza del sottoalbero che ha come radice node.
        Ovvero il numero di livelli di discendenza di quel nodo.
        :param node:
        :return: altezza
        """
        if node is None:
            return -1  # aiuta a calcolare il balance factor
        return node.info[self.HEIGHT_INDEX]
    
    def __setHeight(self, node, h):
        """
        Metodo per settare l'altezza del nodo node al valore h.
        :param node:
        :param h: nuova altezza
        """
        if node is not None:
            node.info[self.HEIGHT_INDEX] = h
    
    def __balanceFactor(self, node):
        """
        Permette di calcolare il fattore di bilanciamento del nodo node.
        :param node:
        :return: fattore di bilanciamento
        """
        if node is None:
            return 0
        return self.__height(node.leftSon) - self.__height(node.rightSon)

    def __updateHeight(self, node):
        """
        Permette di aggiornare l'altezza del nodo node al valore uguale a:
        massima altezza tra le altezza dei due figli, a cui deve essere aggiunto 1.
        :param node:
        """
        if node is not None:
            self.__setHeight(node, max(self.__height(node.leftSon), self.__height(node.rightSon)) + 1)

    def print(self):
        self.tree.print()

    """
        METODI DI ROTAZIONE E BILANCIAMENTO
    """
    def rightRotation(self, v):
        """
        Esegue una rotazione semplice a destra con perno in v
        :param v: perno
        """
        u = v.leftSon
        v.info, u.info = u.info, v.info

        uTree = self.tree.cutLeft(v)
        t1 = uTree.cutLeft(u)
        t2 = uTree.cutRight(u)
        t3 = self.tree.cutRight(v)
        
        uTree.insertAsRightSubTree(uTree.root, t3)
        uTree.insertAsLeftSubTree(uTree.root, t2)
        self.tree.insertAsRightSubTree(v, uTree)
        self.tree.insertAsLeftSubTree(v, t1)
        
        self.__updateHeight(v.rightSon)
        self.__updateHeight(v)
    
    def leftRotation(self, node):
        """
        Esegue una rotazione semplice a destra con perno in node
        :param node: perno
        """
        rightSon = node.rightSon
        node.info, rightSon.info = rightSon.info, node.info
        
        rtree = self.tree.cutRight(node)
        ltree = self.tree.cutLeft(node)
        rtree_l = rtree.cutLeft(rightSon)
        rtree_r = rtree.cutRight(rightSon)
        
        rtree.insertAsLeftSubTree(rtree.root, ltree)
        rtree.insertAsRightSubTree(rtree.root, rtree_l)
        self.tree.insertAsLeftSubTree(node, rtree)
        self.tree.insertAsRightSubTree(node, rtree_r)
        
        self.__updateHeight(node.leftSon)
        self.__updateHeight(node)

    def rotate(self, node):
        """
        Partendo dal nodo node, riesce a capire quale e' il tipo
        di rotazione da effettuare in base al fattore di bilanciamento
        del nodo e de suoi figli. 4 casi:
        1) SS: bf(x) = 2 e bf(x.left) = 1
            rightRotate(x)
        2) SD: bf(x) = 2 e bf(x.left)= -1
            leftRotate(x.left)
            rightRotate(x)
        3) DD: bf(x) = -2 e bf(x.right)= -1
            leftRotate(x)
        4) DS: bf(x) = -2 e bf(x.right)= 1
            rightRotate(x.right)
            leftRotate(x)
        :param node:
        :return:
        """
        balFact = self.__balanceFactor(node)
        if balFact == 2:  # altezza figlio sinistro di node e' piu' grande di 2 rispetto al figlio destro
            if self.__balanceFactor(node.leftSon) >= 0: #sbilanciamento SS
                self.rightRotation(node)
            else: #sbilanciamento SD
                self.leftRotation(node.leftSon)
                self.rightRotation(node)
        elif balFact == -2:  # altezza figlio destro di node e' piu' grande di 2 rispetto al figlio sinistro
            if self.__balanceFactor(node.rightSon) <= 0:  # sbilanciamento DD
                self.leftRotation(node)
            else:  # sbilanciamento DS
                self.rightRotation(node.rightSon)
                self.leftRotation(node)

    def balInsert(self, newNode):
        """
        Partiamo da newNode e risaliamo verso la radice finchè
        incontriamo un nodo critico (se esiste) ed eseguiamo una rotazione
        per bilanciare l'albero
        :param newNode:
        """
        curr = newNode.father
        while curr is not None:
            if abs(self.__balanceFactor(curr)) >= 2:
                break  # ci fermiamo all'UNICO nodo critico (se esiste)
            else:
                self.__updateHeight(curr)
                curr = curr.father
        if curr is not None:
            self.rotate(curr)

    def balDelete(self, removedNode):
        """
        Partiamo da removedNode e risaliamo verso la radice finchè
        incontriamo un nodo critico (se esiste) ed eseguiamo una rotazione
        :param removedNode:
        """
        curr = removedNode.father
        while curr is not None:  # ci potrebbero essere più nodi da bilanciare
            if abs(self.__balanceFactor(curr)) == 2:
                self.rotate(curr)
            else:
                self.__updateHeight(curr)
            curr = curr.father
    
    def cutSingleSon(self, node):
        """
        Rimuoviamo l'unico figlio (se esiste) di node
        ed effettuiamo un bilanciato dell'albero
        :param node:
        :return:
        """
        self.cutOneSonNode(node)
        self.balDelete(node)

    """
    Search(key) è ereditato da BST       O(log(n))
    Insert(key) è leggermente modificata O(log(n))
    Delete(key) è leggermente modificata O(log(n))
    """
    def insert(self, key, value):
        newt = BinaryTree(BinaryNode([key, value, 0]))
        self.insertSingleNodeTree(key, newt)
        self.balInsert(newt.root)       # bilanciare l'albero (se necessario)

    def delete(self, key):
        u = self.searchNode(key)
        if u is not None:
            if len(self.tree.sonsOf(u)) < 2:  # 0 o 1 figlio
                self.cutSingleSon(u)
            else:
                p = self.pred(u)
                u.info, p.info = p.info, u.info
                # si ripristinano le  corrette altezze dei 2 nodi swappati
                th = self.__height(u)  # variabile temporanea
                self.__setHeight(u, self.__height(p))
                self.__setHeight(p, th)
                self.cutSingleSon(p)


if __name__ == "__main__":
    avl = AVLTree()

    data = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]

    for d in data:
        avl.insert(d, d * 2)
        print(f"Inserted ({d}, {d * 2}) tuple")
    avl.print()
    print(f"After {len(data)} insertions, bst has {avl.size()} elements")

    print(f"Pred of node with key 100 {avl.pred(100)}")
    print(f"Pred of node with key 70 {avl.pred(70)}")
    print(f"Tree max from root is {avl.max(avl.tree.root)}")

    data.reverse()
    for s in data:
        print(f"Search for key {s} returned {avl.search(s)}")


    avl.delete(30)
    avl.print()
