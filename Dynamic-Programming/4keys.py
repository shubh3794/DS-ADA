##you have a special kinda keyboard having only 4 keys, 'A', 'Ctrl+A' which selects everything, 'Ctrl+C' which copies the selected buffer
##'Ctrl+V' which pastes the copied buffer. Find the maxm num of 'A's'that can be printed
##in n inputs

def recur(n,m):
    if n<=6:
        return n
    for i in range(1,7):
        m[i-1]=i
    for j  in range(7,n+1):
        for k in range(i-3,0,-1):
            x = (j-k-1)*m[k-1]
            if x > m[j-1]:
                m[j-1]=x
    return m[n-1]


def MaxA():
    n = int(raw_input())
    m = [0]*(n+1)
    print recur(n,m)

MaxA()
