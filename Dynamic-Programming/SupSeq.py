##Given two strings, find the shortest common supersequence such that both the given sequences are sunsequences of the supersequance.
##We will use edit distance except that we wont use replacement operation
import sys
def SCS():
    a = raw_input()
    b = raw_input()
    m = len(a)
    n = len(b)
    T = [[sys.maxint]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0:
                T[i][j] = j

            elif j==0:
                T[i][j] = i
                
            elif a[i-1]==b[j-1]:
                T[i][j] = T[i-1][j-1]+1
            else:
                T[i][j] = 1 + min(T[i-1][j],T[i][j-1])
    x = T[m][n]
    i = m
    j = n
    k = x-1
    s = [None]*x
    while i > 0 and j > 0:
        if a[i-1]==b[j-1]:
             s[k] = a[i-1]
             k -= 1
             i -= 1
             j -= 1
        else:
            if T[i-1][j] < T[i][j-1]:
                s[k] = a[i-1]
                i -= 1
            else:
                s[k] = b[j-1]
                j -= 1
            k -= 1
    print s
    print x            
            
SCS()
                
