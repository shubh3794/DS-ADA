##Classic dice throw problem: given n dices with m faces such that each dice can have faces valued from 1...m
##Find number of ways you can gather a number x from these dices. All dices should be used. For
##example: x = 1 n = 4 m = 3, then num of ways is 0 because each dice has one
##face marked 1. So the min sum that can be gathered from all 4 dices is 4.

def gatherX():
    x = int(raw_input())
    m = int(raw_input())
    n = int(raw_input())
    L = [[0]*(n+1) for i in range(x+1)]
    if x <= m:
        for i in range(1,x+1):
            L[i][1] = 1
    else:
        for i in range(1,m+1):
            L[i][1] = 1
            
    for i in range(2,x+1):
        for j in range(2,n+1):
            for k in range(1,m+1):
                if i-k > 0:
                    L[i][j] += L[i-k][j-1]
    return L[x][n]

print gatherX()
