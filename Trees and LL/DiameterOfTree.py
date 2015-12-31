from BaseClass import BTree
class Height:
    def __init__(self):
        self.h = 0

def FindDia(x,H):
    lh = Height()
    rh = Height()
    if x==None:
        lh.h = 0
        rh.h = 0
        return 0
    lh.h += 1
    rh.h += 1
    ld = FindDia(x.left,lh)
    rd = FindDia(x.right,rh)
    H.h = max(lh.h,rh.h)+1
    return max(lh.h + rh.h + 1, max(ld,rd))

a = BTree()
a.insertL(a.root,9)
a.insertL(a.root,8)
a.insertL(a.root,7)
a.insertL(a.root,6)
a.insertL(a.root,5)
a.insertL(a.root,4)
a.insertL(a.root,3)
a.insertL(a.root,2)
a.insertL(a.root,1)

a.insertR(a.root,0)
a.insertR(a.root,1)
a.insertR(a.root,11)
a.insertR(a.root,14)

s = Height()
print FindDia(a.root,s)

