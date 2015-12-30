from BaseClass import bTree

def LCA(x,left,right):
    if x==None:
        return
    if x == left or x==right:
        return x
    x.left = LCA(x.left,left,right)
    x.right = LCA(x.right,left,right)
    if x.left and x.right:
        return x
    else:
        if x.left:
            return x.left
        if x.right:
            return x.right
