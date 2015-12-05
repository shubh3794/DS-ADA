##given a value(n) and moves as 3,5,10. Find the number of ways we can sum up to
##n using these three moves. Note that 5,10,5 and 5,5,10 and 10,5,5 are counted as same.
##order does not matter

def Count():
    n = int(raw_input())
    m = [0]*(n+1)
    a = [3,5,10]
    for i in range(3):
        m[i]=0
    m[0]=1
    if n < 3:
        return 0
    for i in range(3):
        for j in range(a[i],n+1):
            m[j] += m[j-a[i]]
    return m[n]
    
print Count()
