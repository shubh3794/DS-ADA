class Stack:
    def __init__(self):
        self.top = -1
        self.__stack__ = []

    def push(x):
        self.top += 1
        self.__stack__.append(x)
        return self.__stack__[self.top]

    def pop():
        return self.__stack__.pop()


class Node:
    def __init__(self,data=None):
        self.value = data
        self.left = None
        self.right = None
        self.next = None
        self.previous = None
        self.random = None
    def __str__(self):
        return "Node is %s" % (self.value)
    
class BTree:
    def __init__(self):
        self.root = None

    def insertL(self,x,value):
        self.root = self.insertLeft(self.root,value)
    def insertR(self,x,value):
        self.root = self.insertRight(self.root,value)
    def insertLeft(self,x,value):
        if x==None:
            x = Node(value)
        elif x.left==None:
            x.left = self.insertLeft(x.left,value)
        elif x.right==None:
            x.right = self.insertRight(x.right,value)
        else:
            x.left = self.insertLeft(x.left,value)
        return x
    
    def insertRight(self,x,value):
        if x==None:
            x = Node(value)
        elif x.right==None:
            x.right = self.insertRight(x.right,value)
        elif x.left==None:
            x.left = self.insertLeft(x.left,value)
        else:
            x.right = self.insertRight(x.right,value)
        return x
    def __str__(self):
        return "Root is %s" %(self.root.value)

    

class BST:
    def __init__(self):
        self.root = None

    def ins(self,x,value):
        self.root = self.insert(self.root,value)
        
    def insert(self,x,value):
        if x==None:
            x = Node(value)
        elif x.value <= value:
            x.right = self.insert(x.right,value)
        else:
            x.left = self.insert(x.left,value)
        return x

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enq(self,value):
        node = Node(value)
        if self.rear!=None:
            self.rear.next = node
        self.rear = node
        if self.front ==None:
            self.front = self.rear
            
    def deq(self):
        if self.isEmpty():
            return
        temp = self.front.value
        self.front = self.front.next
        if self.front == None:
            self.rear=None
        print temp    
        return temp

    def isEmpty(self):
        if self.front==None:
            return True
        else:
            return False
        
       
