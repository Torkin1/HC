"""
    File name: Stack.py
    Author: Domenico Spera
    Date created: 11/10/2016
    Modified By: Laura Trivelloni
    Date last modified: 15/10/2017
    Python Version: 3.5.2

    This module implements a structure data and its methods to insert, delete, visualize an item,
    check if the list is empty and print all items following a LIFO scheduling.
"""

from list.LinkedList import ListaCollegata


""" 
    Not strictly necessary. It is just an example to show how you could simulate interfaces 
    behavior in Python (and related stuff!).
"""


class Pila:

    def push(self, elem):
        raise NotImplementedError("You should have implemented this method!")

    def pop(self):
        raise NotImplementedError("You should have implemented this method!")

    def top(self):
        raise NotImplementedError("You should have implemented this method!")

    def isEmpty(self):
        raise NotImplementedError("You should have implemented this method!")


"""
    Stack implemented using a linked list.
"""
class PilaListaCollegata(ListaCollegata, Pila):  # Multiple inheritance!
    # WATCH: not explicitly overridden methods of Pila are implicitly overridden by ListaCollegata!
    # Override
    def push(self, elem):
        self.addAsFirst(elem)

    # Override
    def pop(self):
        return self.popFirst()

    # Override
    def top(self):
        return self.getFirst()


"""
    Stack implemented using a built-in list. "Naive" way.
"""


class PilaArrayList_dummy(Pila):

    def __init__(self):
        self.s = []

    # Override
    def push(self, elem):
        self.s.insert(0, elem)

    # Override
    def pop(self):
        if len(self.s) == 0:
            return None
        return self.s.pop(0)

    # Override
    def top(self):
        if len(self.s) == 0:
            return None
        return self.s[0]

    # Override
    def isEmpty(self):
        return len(self.s) == 0

    def printOrdered(self):
        print("Elements in the collection (ordered):")
        print(self.s)


"""
    Stack implemented using a built-in list.
"""


class PilaArrayList(Pila):
    def __init__(self):
        self.s = []

    # Override
    def push(self, elem):
        self.s.append(elem)

    # Override
    def pop(self):
        if len(self.s) == 0:
            return None
        return self.s.pop()

    # Override
    def top(self):
        if len(self.s) == 0:
            return None
        return self.s[-1]

    # Override
    def isEmpty(self):
        return len(self.s) == 0

    def printOrdered(self):
        print("Elements in the collection (ordered):")
        print(self.s)


# global functions
def testStack(s):
    # This is a way to impose restrictions on the types of the arguments,
    # using inheritance and polymorphism. (Not strictly necessary in Python)
    if not isinstance(s, Pila):
        raise TypeError("Expected type was Pila.")

    for i in range(10):
        s.push(i)
    s.printOrdered()

    print("Top:", s.top())
    print("Pop:", s.pop())
    print("Top:", s.top())
    print("Pop:", s.pop())
    print("Top:", s.top())
    s.printOrdered()


# to run this module directly (NOT imported in another one)
if __name__ == "__main__" :

    print("Pila - Lista Collegata")
    s = PilaListaCollegata()
    testStack(s)

    print("Pila - ArrayList_dummy")
    s = PilaArrayList_dummy()
    testStack(s)

    print("Pila - ArrayList")
    s = PilaArrayList()
    testStack(s)
