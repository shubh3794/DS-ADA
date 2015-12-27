import sys
from BaseClass import Node
from random import randint

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insertBeg(self,data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp
        if self.head.next == None:
            self.tail = self.head
        return self.head

    def insertEnd(self,data):
        temp = Node(data)
        temp.next = None
        self.tail.next = temp
        self.tail = temp
        return self.tail

    def insertAtPos(self,data,pos):
        temp = Node(data)
        count = 1
        curr = self.head
        while count < pos-1:
            curr = curr.next
            count += 1
        storeNext=curr.next
        curr.next = temp
        temp.next = storeNext

    def delete(self):
        if self.head.next = None:
            self.tail = None
        self.head = self.head.next
        return self.head

    def reversePrint(self,x):
        if x == None:
            return
        reversePrint(self,x.next)
        print x
        
    
