from BaseClass import Node
from BTreeAndBST import inorder
class LL:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self,value):
        temp = self.head
        x = Node(value)
        x.prev = temp
        self.head = x
        if self.tail == None:
            self.tail = x
        else:
            temp.next = x
    def delete(self):
        if self.head == None:
            return
        if self.head == self.tail:
            self.tail = self.tail.prev
        self.head = self.head.prev
        return

def findMid(head):
    slowptr = head
    fastptr = head
    while fastptr.next!=None and fastptr.next.next!=None:
        slowptr = slowptr.next
        fastptr = fasptr.next.next
    return slowptr

lis = LL()
for i in range(10):
    lis.insert(i)

def LLBST(x):
    if x==None:
        return
    temp = findMid(x)
    left = temp.prev
    right = temp.next
    temp.prev = None
    if left:
        left.next = None
    if right:
        right.prev = None
    temp.next = None
    a = LLBST(left)
    b = LLBST(right)
    temp.left = a
    temp.right = b
    return temp
root = LLBST(lis.head)

inorder(root)
        
        
        
