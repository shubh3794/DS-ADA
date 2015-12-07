
def  maxDifference( a):
    n = len(a)
    m = [-1]*n
    maxi = -1
    for i in range(1,n):
        for j in range(0,i):
            global maxi
            m[i] = max(m[i],a[i]-a[j])
            if m[i]>maxi:
                maxi=m[i]
    return maxi

a =  map(int,raw_input().split())
print maxDifference(a)
