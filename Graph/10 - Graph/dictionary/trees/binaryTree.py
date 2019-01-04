"""
    File name: binaryTree.py
    Author: Ovidiu Daniel Barba
    Date created: 14/11/2018
    Date last modified: 14/11/2018
    Python Version: 3.7

    Questo modulo contiene implementazione di alberi binari
"""

from dictionary.trees.tree import Tree as Tree
from datastruct.Stack import PilaArrayList as Pila
from datastruct.Queue import CodaArrayList_deque as Queue


class BinaryNode:
    """
    Classe che rappresenta un nodo di un albero binario
    """
    def __init__(self, info):
        """
        :param info: una struttura dati qualsiasi (lista, dizionario, ecc)
        o una semplice variabile. Permette di aggiungere informazioni
        aggiuntive
        """
        self.info = info
        self.father = None
        self.leftSon = None
        self.rightSon = None

    def __str__(self):
        return str(self.info)

    def __repr__(self):
        return self.__str__()


class BinaryTree(Tree):
    """
    Classe che rappresenta un albero binario i cui
    nodi sono istanza di BinaryNode
    """
    def __init__(self, root=None):
        """
        :param root: radice dell'albero. Se non  specificata,
        albero vuoto
        """
        self.root = root
        self.n = 0   # albero con 0 elementi
        if root is not None:  # aggiorna n se viene passata una radice non nulla (albero non vuoto)
            self.__increaseNodesNumberBySubtree(root)

    def isLeaf(self, node):
        """
        :param node:
        :return: True se node è una foglia, False altrimenti
        """
        if len(self.sonsOf(node)) == 0:
            return True
        return False

    def __increaseNodesNumberBySubtree(self, node):
        """
        incrementa il numero di nodi nell'albero con il
        numero dei nodi del sottoalbero radicato in node
        :param node:
        """
        self.n += self.__subtreeNodesNumber(node)

    def __decreaseNodesNumberBySubtree(self, node):
        """
        decrementa il numero di nodi nell'albero con il
        numero dei nodi del sottoalbero radicato in node
        :param node:
        """
        self.n -= self.__subtreeNodesNumber(node)

    def __subtreeNodesNumber(self, node):
        """
        :param node: radice del sottoalbero
        :return: numero di nodi del sottoalbero radicato in node
        """
        res = []
        stack = Pila()
        if node is not None:
            stack.push(node)
        while not stack.isEmpty():
            current = stack.pop()
            res.append(current.info)
            if current.rightSon is not None:
                stack.push(current.rightSon)
            if current.leftSon is not None:
                stack.push(current.leftSon)
        return len(res)

    def insertAsLeftSubTree(self, father, subtree):
        """
        Permette di inserire la radice di un sottoalbero come figlio sinistro
        del nodo father
        :param father: nodo su cui attaccare subtree
        :param subtree: da inserire
        """
        son = subtree.root
        if son is not None:
            son.father = father
            self.__increaseNodesNumberBySubtree(son)
        father.leftSon = son

    def insertAsRightSubTree(self, father, subtree):
        """
        Permette di inserire la radice di un sottoalbero come figlio destro
        del nodo father
        :param father: nodo su cui attaccare subtree
        :param subtree: da inserire
        """
        son = subtree.root
        if son is not None:
            son.father = father
            self.__increaseNodesNumberBySubtree(son)
        father.rightSon = son

    def cutLeft(self, father):
        """
        Permette di rimuovere l'intero sottoalbero che parte dal figlio
        sinistro del nodo father
        :param father:
        :return: sottoalbero radicato nel figlio sinistro di father
        """
        son = father.leftSon
        newTree = BinaryTree(son)
        self.__decreaseNodesNumberBySubtree(son)
        father.leftSon = None
        return newTree

    def cutRight(self, father):
        """
        Permette di rimuovere l'intero sottoalbero che parte dal figlio
        destro del nodo father
        :param father:
        :return: sottoalbero radicato nel figlio destro di father
        """
        son = father.rightSon
        newTree = BinaryTree(son)
        self.__decreaseNodesNumberBySubtree(son)
        father.rightSon = None
        return newTree

    """
        METODI EREDITATI DALLA CLASSE TREE.
        VEDERE LA CLASSE PER DESCRIZIONE DEI METODI
    """
    def cut(self, node):
        if node is None:
            return BinaryTree(None)
        if node.father is None:  # nodo radice
            self.root = None
            self.n = 0  # se stacco la radice, l'albero è vuoto
            return BinaryTree(node)
        f = node.father
        if self.isLeaf(node):  # a leaf!
            if f.leftSon == node:
                f.leftSon = None
            else:
                f.rightSon = None
            self.n -= 1    # è una foglia quindi n diminuisce di 1
            return BinaryTree(node)
        elif f.leftSon == node:
            nt = self.cutLeft(f)
            # f.leftSon = None  --> Questa operazione viene fatta in cutLeft
            return nt
        else:
            nt = self.cutRight(f)
            # f.rightSon = None  --> Questa operazione viene fatta in cutRight
            return nt

    def nodesNumber(self):
        return self.n

    def fatherOf(self, node):
        if node is None:
            return None
        return node.father

    def sonsOf(self, node):
        sons = []
        if node is None:
            return sons
        if node.leftSon is not None:
            sons.append(node.leftSon)
        if node.rightSon is not None:
            sons.append(node.rightSon)
        return sons

    def degree(self, node):
        return len(self.sonsOf(node))

    def print(self):
        """
        Permette di stampare l'albero. Per farlo si usa una pila di appoggio
        """
        stack = Pila()
        if self.root is not None:
            stack.push([self.root, 0])  # pila di liste di due elementi [il nodo, il livello occupato dal nodo]
            print("-- Tree --")
        else:
            print("Empty tree!")
            return
        while not stack.isEmpty():
            current = stack.pop()
            level = current[1]
            print("|---" * level + str(current[0].info))

            if current[0].rightSon is not None:
                stack.push([current[0].rightSon, level + 1])
            if current[0].leftSon is not None:
                stack.push([current[0].leftSon, level + 1])
        print("-- Tree End -- ")

    def DFS(self):
        """
        Permette di restituire una lista di elementi ottenuta da una visita
        in profondità dell'albero.
        :return: list nodi
        """
        res = []
        stack = Pila()
        if self.root is not None:
            stack.push(self.root)
        while not stack.isEmpty():
            current = stack.pop()
            res.append(current.info)
            if current.rightSon is not None:
                stack.push(current.rightSon)
            if current.leftSon is not None:
                stack.push(current.leftSon)
        return res

    def BFS(self):
        """
        Permette di restituire una lista di elementi ottenuta da una visita
        in ampiezza dell'albero.
        :return: lista nodi
        """
        res = []
        q = Queue()
        if self.root is not None:
            q.enqueue(self.root)
        while not q.isEmpty():
            current = q.dequeue()
            res.append(current.info)
            if current.leftSon is not None:
                q.enqueue(current.leftSon)
            if current.rightSon is not None:
                q.enqueue(current.rightSon)
        return res


if __name__ == "__main__":

    t = BinaryTree(BinaryNode(1))
    t.insertAsLeftSubTree(t.root,                   BinaryTree(BinaryNode(2)))
    t.insertAsRightSubTree(t.root,                  BinaryTree(BinaryNode(3)))
    t.insertAsLeftSubTree(t.root.leftSon,           BinaryTree(BinaryNode(4)))
    t.insertAsRightSubTree(t.root.leftSon,          BinaryTree(BinaryNode(5)))
    t.insertAsRightSubTree(t.root.rightSon,         BinaryTree(BinaryNode(6)))
    t.insertAsLeftSubTree(t.root.leftSon.leftSon,   BinaryTree(BinaryNode(7)))
    print(f"Tree has {t.nodesNumber()} nodes")
    t.print()
    print(f"Sons of root are {t.sonsOf(t.root)}")
    print(f"Root's degree is {t.degree(t.root)}")
    t.cutLeft(t.root)
    print("Deleted left subtree from root")
    print(f"{t.nodesNumber()} nodes left")
    t.print()
    print(f"Root's degree is now {t.degree(t.root)}")
    t.cut(t.root)
    print("Removed subtree in root with cut() method")
    print(f"{t.nodesNumber()} nodes left")


