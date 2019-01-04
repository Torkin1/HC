"""
    File name: binarySearchTree.py
    Author: Ovidiu Daniel Barba
    Date created: 14/11/2018
    Date last modified: 14/11/2018
    Python Version: 3.7

    Questo modulo contiene l'implementazione
    dell'albero binario di ricerca (BST)
"""

from dictionary.trees.binaryTree import *
from dictionary.Dictionary import Dictionary


class BinarySearchTree(Dictionary):
    """
    Un albero binario di ricerca e' un albero che soddisfa le seguenti proprieta':
    1. ogni nodo v contiene un valore (info[1]) cui e' associata una chiave (info[0])
        presa da n dominio totalmente ordinato.
    2. Le chiavi nel sottoalbero sinistro di v sono <= chiave(v).
    3. Le chiavi nel sottoalbero destro di v sono >= chiave(v).
    """
    KEY_INDEX = 0    # indici usati per trovare le relative informazioni da un nodo
    VALUE_INDEX = 1  # nodo.info[KEY_INDEX] è la chiave del nodo

    def __init__(self):
        self.tree = BinaryTree()  # node's info now is a list [key, value]
    
    def __key(self, node):
        """
        Permette di ritornare la chiave associata ad un nodo
        :param node:
        :return: chiave (se nodo non nullo). None altrimenti
        """
        if node is None:
            return None
        return node.info[self.KEY_INDEX]
    
    def __value(self, node):
        """
        Permette di ritornare il valore associato ad un nodo
        :param node:
        :return: valore (se nodo non nullo). None altrimenti
        """
        if node is None:
            return None
        return node.info[self.VALUE_INDEX]

    def __isLeftSon(self, node):
        """
        :param node: figlio
        :return: True se il nodo node è il figlio sinistro del proprio
                 padre, False altrimenti
        """
        if node == node.father.leftSon:
            return True
        return False

    def searchNode(self, key):
        """
        Permette di ricercare il nodo con chiave key all'interno del dizionario.
        Ritorna il nodo, oppure None se non esiste un nodo associato a key
        :param key:
        :return: nodo (se esiste) con chiave key
        """

        if self.tree.root is None:
            return None  # albero vuoto
        
        curr = self.tree.root
        while curr is not None:
            ck = self.__key(curr)
            if key == ck:
                return curr  # trovato!
            # ricerca binaria
            if key < ck:
                curr = curr.leftSon
            else:
                curr = curr.rightSon
        
        return None

    def cutOneSonNode(self, node):  # contrai un nodo con un singolo figlio
        """
        Permette di cancellare un nodo dall'albero, sapendo che il nodo
        che si sta cancellando ha al massimo un solo figlio.
        :param node:
        """
        son = None
        if node.leftSon is not None:
            son = node.leftSon
        elif node.rightSon is not None:
            son = node.rightSon

        if son is None:
            self.tree.cut(node)  # it's a leaf
        else:
            node.info, son.info = son.info, node.info  # swap info
            nt = self.tree.cut(son)
            self.tree.insertAsLeftSubTree(node, nt.cut(son.leftSon))
            self.tree.insertAsRightSubTree(node, nt.cut(son.rightSon))

    def max(self, node):
        """
        Permette di ottenere il nodo figlio con chiave piu' grande
        del sottoalbero radicato in node. Il nodo con chiave
        piu' grande e' quello che si trova piu' a destra possibile
        O(h)
        :param node:
        :return: figlio con chiave più grande
        """
        curr = node
        while curr.rightSon is not None:
            curr = curr.rightSon
        return curr

    def pred(self, node):
        """
        Ricerca del predecessore di un nodo u in un BST   O(h)
        Si hanno due casi:
        1) se u ha il figlio sinistro, allora pred(u) è il massimo del
           sottoalbero sinistro di u
        2) u non ha il figlio sinistro, allora pred(u) è il più basso
           antenato di u il cui figlio destro è anch'esso antenato di u
        :param node:
        :return: predecessore di node
        """
        # if we pass a node (instance of BinaryNode), we use it as u, else
        # we pass a key and we first search for the node with that key and
        # then assign it to u
        u = node if isinstance(node, BinaryNode) else self.searchNode(node)
        if u is None:  # maybe it's not present in the tree
            return None
        if u.leftSon is not None:
            return self.max(u.leftSon)
        curr = u
        while curr.father is not None and self.__isLeftSon(curr):
            curr = curr.father
        return curr.father

    def size(self):
        """
        :return: number of elements in dictionary
        """
        return self.tree.nodesNumber()

    def print(self):
        self.tree.print()

    """
        METODI EREDITATI DA DICTIONARY
    """

    def search(self, key):
        """
        Permette di ottenere il valore associato alla chiave key presente
        all'interno dell'albero
        O(h)
        :param key:
        :return: valore del nodo con chiave key (se esiste)
        """
        node = self.searchNode(key)
        return self.__value(node)

    def insertSingleNodeTree(self, key, newt):
        if self.tree.root is None:
            self.tree.root = newt.root  # albero vuoto, aggiungi come radice
            self.tree.n += 1            # aumenta di 1 il numero dei nodi dell'albero
        else:
            curr = self.tree.root
            pred = None             # nodo precedente che abbiamo analizzato
            while curr is not None:
                pred = curr
                if key <= self.__key(curr):  # ricerco il futuro padre di key
                    curr = curr.leftSon
                else:
                    curr = curr.rightSon

            # pred adesso punta al futuro padre di key
            # inseriamo a sinistra o a destra del padre
            # per mantenere la proprietà di ricerca
            if key <= self.__key(pred):
                self.tree.insertAsLeftSubTree(pred, newt)
            else:
                self.tree.insertAsRightSubTree(pred, newt)
    
    def insert(self, key, value):
        """
        Permette di inserire un valore all'interno del dizionario
        nella maniera corretta
        O(h)
        :param key:
        :param value:
        """
        tree = BinaryTree(BinaryNode([key, value]))
        self.insertSingleNodeTree(key, tree)


    def delete(self, key):
        """Permette di cancellare (se esiste) il nodo u con chiave key.
        Prima di cancellarlo bisogna fare la search per trovarlo
        e successivamente distinguere 3 casi:
        1) u è foglia
        2) u ha 1 solo figlio v: se u è la radice, v diviene la nuova radice,
           altrimenti v viene direttamente attaccato al padre di u
        3) u ha 2 figli
        O(h)
        :param key:
        :return:
        """
        u = self.searchNode(key)
        if u is not None:
            if len(self.tree.sonsOf(u)) < 2:     # sto rimuovendo un nodo che ha 0 o 1 figlio
                self.cutOneSonNode(u)
            else:                                # sto rimuovendo un nodo che ha due nodi figli
                p = self.pred(u)                 # predecessore del nodo da rimuovere
                u.info, p.info = p.info, u.info  # scambio il contenuto informativo dei nodi
                self.cutOneSonNode(p)          # adesso so che p non ha figli destri e posso applicare la cutOneSonNode


if __name__ == "__main__":

    bst = BinarySearchTree()

    data = [100, 90, 110, 70, 140, 50, 40, 200, 130, 125, 135, 132]

    for d in data:
        bst.insert(d, d * 2)
        print(f"Inserted ({d}, {d * 2}) tuple")

    data.reverse()
    for s in data:
        print(f"Search for key {s} returned {bst.search(s)}")

    bst.print()
    print(f"After {len(data)} insertions, bst has {bst.size()} elements")

    print(f"Pred of node with key 140 {bst.pred(140)}")
    print(f"Pred of node with key 125 {bst.pred(125)}")
    print(f"Tree max from root is {bst.max(bst.tree.root)}")

    bst.delete(40)
    print(f"Deleted leaf 40")
    bst.print()

    bst.delete(110)
    print(f"Deleted internal node 110 with only 1 child")
    bst.print()

    bst.delete(140)
    print(f"Deleted internal node 140 with 2 children")
    bst.print()



