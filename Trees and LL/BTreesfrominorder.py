from BaseClass import Node
inorder_arr = map(int,raw_input().split())
def getBtree(start,end,arr):
    if start>end:
        return [None]
    trees = []
    for i in range(start,end+1):
        getL = getBtree(start,i-1,arr)
        getR = getBtree(i+1,end,arr)
        for j in getL:
            for k in getR:
                root = Node(arr[i])
                root.left = j
                root.right = k
                trees.append(root)
    return trees
def preorder(x):
    if x==None:
        return
    print x.value,
    preorder(x.left)
    preorder(x.right)
    
def ans(arr):
    gettrees = getBtree(0,len(arr)-1,arr)
    for i in gettrees:
        preorder(i)
        print "\n"

ans(inorder_arr)
