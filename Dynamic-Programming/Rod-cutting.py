##rod cutting, given an n-length rod and an array containing selling price of rods of length 1...n
##find max possible sp attainable by cutting the rod and selling it

def RodCutting():
    x = int(raw_input())
    a = map(int,raw_input().split())
    n = len(a)
    m = [0]*(x+1)
    for i in range(1,x+1):
        m[i]=m[i-1]
        for j in range(1,n+1):
            if i-j>=0:
                q = m[i-j]+a[j-1]
                if q > m[i]:
                    m[i] = q
    return m[x]

print RodCutting()
