from BTreeAndBST import bTree,inorder

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
convertMirror(bTree.root)
print "\n Mirror"
inorder(bTree.root)
