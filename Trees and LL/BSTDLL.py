from BaseClass import BST
from BTreeAndBST import inorder
tree = BST()
tree.ins(tree.root,6)
tree.ins(tree.root,2)
tree.ins(tree.root,4)
tree.ins(tree.root,0)
tree.ins(tree.root,3)
tree.ins(tree.root,5)
tree.ins(tree.root,1)
tree.ins(tree.root,-1)

tree.ins(tree.root,8)
tree.ins(tree.root,7)
tree.ins(tree.root,10)
tree.ins(tree.root,9)
tree.ins(tree.root,11)
inorder(tree.root)
print "\n"

##N^2 complexity
def BSTDLL(x,flag):
    if x==None:
        return
    if x.left==None and x.right==None:
        return x
    l=None
    r=None
    if x.left:
        l = BSTDLL(x.left,'r')
    if x.right:
        r = BSTDLL(x.right,'l')
    if l:
        l.next = x
        x.prev = l
    if r:
        x.next = r
        r.prev = x

    if flag=='r':
        if r==None:
            r = x
        while r.next!=None:
            r = r.next
        return r
    if flag=='l':
        if l==None:
            l = x
        while l.prev!=None:
            l = l.prev
        return l
m = BSTDLL(tree.root,'l')


##N complexity
class NP:
    def __init__(self):
        self.head = None
        self.tail = None
        
def BSDLL(x,result):
    if x==None:
        return
    BSDLL(x.left,result)
    x.left = result.tail
    if result.head != None:
        result.tail.right = x
    else:
        result.head = x
    r = x.right
    x.right = None
    result.tail = x
    BSDLL(r,result)
    
result = NP()
BSDLL(tree.root,result)
curr = result.head
while curr!=None:
    print curr.value
    curr = curr.right
