from BaseClass import BTree, BST
bTree = BTree()
bs = BST()
bTree.insertL(bTree.root,2)
bTree.insertL(bTree.root,3)
bTree.insertR(bTree.root,4)
bTree.insertL(bTree.root,5)
bTree.insertL(bTree.root,6)
bTree.insertR(bTree.root,7)

for i in range(10):
    bs.ins(bs.root,i)

def inorder(x):
    if x==None:
        return
    if x.left != None:
        inorder(x.left)
    print x
    if x.right != None:
        inorder(x.right)
def preorder(x):
    if x==None:
        return
    print x
    if x.left !=None:
        preorder(x.left)
    elif x.right!=None:
        preorder(x.right)

def postorder(x):
    if x==None:
        return
    if x.left !=None:
        preorder(x.left)
    elif x.right!=None:
        preorder(x.right)
    print x

