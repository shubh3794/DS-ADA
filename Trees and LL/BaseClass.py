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



class BST:
    