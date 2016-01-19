a = raw_input()
a = list(a)
def recurPerm(a,ind,res):
    if len(res)==len(a):
        print res
        return
    for i in range(len(a)):
        if i not in ind:
            k = res
            res += a[i]
            ind.append(i)
            recurPerm(a,ind,res)
            res = k
            ind.pop()

recurPerm(a,[],'')
    
