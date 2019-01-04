"""
    File name: Queue.py
    Author: Domenico Spera
    Date created: 11/10/2016
    Modified By: Laura Trivelloni
    Date last modified: 15/10/2017
    Python Version: 3.5.2

    This module implements a structure data and its methods to insert, delete, visualize an item,
    check if the list is empty and print all items following a FIFO scheduling.
"""

from collections import deque
import sys
import os

sys.path.append(str(os.environ.get("PYTHONPATH")) + "/Lez2/")
# to import a library from a directory that isn't the current one
# it needs to specify the path
# $PYTHONPATH is the environment variable containing the project home

from list.LinkedList import ListaCollegata

"""
    Implementation of a FIFO queue using a linked list.
"""


class CodaListaCollegata(ListaCollegata):
    def enqueue(self, elem):
        self.addAsLast(elem)

    def dequeue(self):
        return self.popFirst()


"""
    Implementation of a FIFO queue using a Python's list built-in type, 
    i.e., lists based on array implementation.
"""


class CodaArrayList():
    def __init__(self):
        self.q = []

    def enqueue(self, elem):
        self.q.append(elem)

    def dequeue(self):
        if len(self.q) == 0:
            return None
        return self.q.pop(0)

    def getFirst(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[0]

    def isEmpty(self):
        return len(self.q) == 0

    def printOrdered(self):
        print("Elements in the collection (ordered):")
        print(self.q)


"""
    Faster implementation of a FIFO using the type deque, optimized also for removing elements 
    at the beginning of the collection.
"""


class CodaArrayList_deque(CodaArrayList):
    def __init__(self):
        super().__init__()
        self.q = deque()

    # Override
    def dequeue(self):
        if len(self.q) == 0:
            return None
        return self.q.popleft()


# global functions
def testQueue(q):
    for i in range(10):
        q.enqueue(i)
    q.printOrdered()

    print("First:", q.getFirst())
    print("Dequeue:", q.dequeue())
    print("First:", q.getFirst())
    print("Dequeue:", q.dequeue())
    print("First:", q.getFirst())

    q.printOrdered()


# to run this module directly (NOT imported in another one)
if __name__ == "__main__":
    print("Coda - ListaCollegata")
    q = CodaListaCollegata()
    testQueue(q)

    print("Coda - ArrayList")
    q = CodaArrayList()
    testQueue(q)

    print("Coda - ArrayList_deque")
    q = CodaArrayList_deque()
    testQueue(q)
