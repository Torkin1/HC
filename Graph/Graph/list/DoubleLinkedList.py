"""
    File name: DoubleLinkedList.py
    Author: Domenico Spera
    Date created: 11/10/2016
    Modified By: Laura Trivelloni
    Date last modified: 15/10/2017
    Python Version: 3.5.2

    This module implements a list where each item maintains a double reference to the previous
    item and to the next one and methods to check if the list is empty, print all items,
    get the first/last item, add a new item at the top/bottom, visualize the item at the top/bottom.
"""

import list.LinkedList as LinkedList


class DoubleRecord(LinkedList.Record):
    def __init__(self, elem):
        LinkedList.Record.__init__(self, elem)
        self.prev = None


class ListaDoppiamenteCollegata(LinkedList.ListaCollegata):
    def addAsLast(self, elem):
        rec = DoubleRecord(elem)
        if self.first == None:
            self.first = self.last = rec
        else:
            rec.prev = self.last
            self.last.next = rec
            self.last = rec

    def addAsFirst(self, elem):
        rec = DoubleRecord(elem)
        if self.first == None:
            self.first = self.last = rec
        else:
            self.first.prev = rec
            rec.next = self.first
            self.first = rec

    def popFirst(self):
        if self.first == None:
            return None
        else:
            res = self.first.elem
            self.first = self.first.next
            if self.first != None:
                self.first.prev = None  # Il controllo serve a gestire il caso di lista vuota
            else:
                self.last = None
            return res

    # Now the last item can be deleted efficiently
    def popLast(self):
        if self.first == None:
            return None
        else:
            res = self.last.elem
            self.last = self.last.prev
            if self.last != None:
                self.last.next = None
            else:
                self.first = None
            return res

    # Now any item can be deleted efficiently
    def deleteRecord(self, rec):
        if rec == None:
            return  # restituisce None!
        if rec.prev != None:
            rec.prev.next = rec.next
        else:
            self.first = rec.next
        if rec.next != None:
            rec.next.prev = rec.prev
        else:
            self.last = rec.prev

    def __len__(self):
        size = 0
        curr = self.first
        while curr is not None:
            size += 1
            curr = curr.next
        return size

    def __str__(self):
        s = "["
        current = self.first
        while current is not None:
            if len(s) > 1:
                s += ", "
            s += str(current.elem)
            current = current.next
        s += "]"
        return s


# to run this module directly (NOT imported in another one)
if __name__ == "__main__":
    l = ListaDoppiamenteCollegata()
    l.printOrdered()

    print("addAsFirst(2)")
    l.addAsFirst(2)
    print("addAsFirst(3)")
    l.addAsFirst(3)
    print("addAsLast(4)")
    l.addAsLast(4)
    l.printOrdered()

    print("getFirst()", l.getFirst())
    print("getLast()", l.getLast())
    l.printOrdered()
    print("popFirst()", l.popFirst())
    l.printOrdered()
    print("findFirst()=", l.getFirst())
    print("popFirst()", l.popFirst())
    print("popFirst()", l.popFirst())
    l.printOrdered()
    print("findLast()=", l.getLast())

    print("rec1=insertFirst(2)")
    l.addAsFirst(2)
    rec1 = l.getFirstRecord()
    print("rec2=insertFirst(3)")
    l.addAsFirst(3)
    rec2 = l.getFirstRecord()
    print("rec3=insertLast(4)")
    l.addAsLast(4)
    rec3 = l.getLastRecord()
    l.printOrdered();
    print("delete(rec1)")
    l.deleteRecord(rec1)
    l.printOrdered()
    print("delete(rec2)")
    l.deleteRecord(rec2)
    l.printOrdered()
    print("delete(rec3)")
    l.deleteRecord(rec3)
    l.printOrdered()
