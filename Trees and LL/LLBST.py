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

max = None
def findMax(x):
    global max
    if x==None:
        return
    if max==None:
        max = x
    elif x.value>max.value:
        max = x
    findMax(x.left)
    findMax(x.right)
    return max

def delete(x,val):
    global findMax
    if x==None:
        return
    if x.value < val:
        x.right = delete(x.right,val)
    elif x.value>val:
        x.left = delete(x.left,val)
    else:
        if x.right and x.left:
            temp = findMax(x.left)
            x.value = temp.value
            x.left =  delete(x.left,temp.value)
        else:
            if x.left:
                x = x.left
            elif x.right:
                x = x.right
            else:
                x = None
    return x
        
def RangePrint(x,p,q):
    if x==None:
        return
    if x.value<p:
        RangePrint(x.right,p,q)
    elif x.value > p:
        RangePrint(x.left,p,q)
    if x.value>=p and x.value<=q:
        print x.value,

RangePrint(root,4,11)
       
        
