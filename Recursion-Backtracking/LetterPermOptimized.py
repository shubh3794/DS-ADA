a = raw_input()
a= list(a)
def reverse(a,f,l):
    while f<l:
        temp = a[l]
        a[l] = a[f]
        a[f] = temp
        f+=1
        l-=1
    return a

def findFirst(res):
    for i in range(len(res)-2,-1,-1):
        if a[i]<a[i+1]:
            return i
def findCeil(x,ff,lo,hi):
    ceil = lo
    for i in range(lo,hi):
        if x[ceil] > x[i] and x[i]>ff:
            ceil = i
    return ceil

def sortPerm(a):
    res = a
    res.sort()
    print ''.join(res),
    x = findFirst(res)
    while x!=None:
        y = findCeil(res,res[x],x+1,len(res))
        temp = res[x]
        res[x]=res[y]
        res[y]=temp
        res =reverse(res,x+1,len(res)-1)
        print ''.join(res),
        x = findFirst(res)
    
    
sortPerm(a)
