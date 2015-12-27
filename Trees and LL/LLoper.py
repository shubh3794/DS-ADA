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
        if self.head.next == None:
            self.tail = None
        self.head = self.head.next
        return self.head

    def printLL(self):
        curr = self.head
        while curr !=None:
            print curr
            curr = curr.next

    ##This does not reverses the linked list, this just prints the reverse list
    def reversePrint(self,x):
        if x == None:
            return
        self.reversePrint(x.next)
        print x
        

    ##This actually reverses linked list physically
    def reverseLLInPlace(self,x,end):
        if x == None:
            return
        if x.next==None:
            self.head=x
        temp = x.next
        x.next = end
        end = x
        self.reverseLLInPlace(temp,x)

a = LinkedList()
for i in range(6):
    a.insertBeg(i)
a.reverseLLInPlace(a.head,None)
a.printLL()


        
        
    
