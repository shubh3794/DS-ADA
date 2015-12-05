##given n. and n jobs of type (starttime,endtime,profit). Find the max profit
##scheduling the jobs such that no two jobs overlapd


def findLastValid(turn,m):
    for i in range(turn-1,-1,-1):
        if m[i][1]<=m[turn][0]:
            return m[i][2]
    return -1


def Schedule():
    n = int(raw_input())
    m = []
    for i in range(n):
        m.append(map(int,raw_input().split()))
    t = [0]*(n+1)
    for i in range(1,n+1):
        op1 = m[i-1][2]
        last = findLastValid(i-1,m)
        if last!=-1:
            op1+=last
        t[i] = max(t[i-1],op1)
    return t[n]

print Schedule()

    
