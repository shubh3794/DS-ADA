from BTreeAndBST import bTree,inorder
from BaseClass import Queue
def convertMirror(x):
    if x==None:
        return
    temp = x.left
    x.left = x.right
    x.right = temp
    convertMirror(x.left)
    convertMirror(x.right)
    return x

inorder(bTree.root)



def reverLO():
    arr = []
    queue = Queue()
    queue.enq(bTree.root)
    while queue.isEmpty() == False:        
        x = queue.deq()
        arr.append(x)
        if x.right:
            queue.enq(x.right)
        if x.left:
            queue.enq(x.left)

    while len(arr)!=0:
        x = arr.pop()
        print x.value
    
reverLO()
