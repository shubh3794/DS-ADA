## print the sum of all nodes in diagonal in a binary tree

from BTreeAndBST import bTree

diagonalSum = {}

def assignWeight(x,weight):
    if x==None:
        return
    x.weight = weight
    if weight in diagonalSum:
        diagonalSum[weight]+=x.value
    else:
        diagonalSum[weight] = x.value
        
    x.left = assignWeight(x.left,weight+1)
    x.right = assignWeight(x.right,weight)
    return x

assignWeight(bTree.root,0)

for i in diagonalSum:
    print diagonalSum[i],
