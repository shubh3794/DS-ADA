from BaseClass import BTree, BST
bTree = BTree()
bs = BST()
bTree.insertLeft(bTree.root,2)
bTree.insertLeft(bTree.root,3)
bTree.insertRight(bTree.root,4)
bTree.insertLeft(bTree.root,5)
bTree.insertLeft(bTree.root,6)
bTree.insertRight(bTree.root,7)


for i in range(10):
    bs.insert(bs.head,i)

def inorder(x):
    if x==None:
        return
    if x.left != None:
        inorder(x.left)
    print x
    if x.right != None:
        inorder(x.right)


print "\n btree inorder"
inorder(bTree.head)
print "\n bst inorder"
inorder(bs.head)
