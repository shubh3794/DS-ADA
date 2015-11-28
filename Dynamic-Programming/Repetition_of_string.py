##Given two strings, shorter string is s, longer is t, find the number of times
##s appears in t. We will solve this by bottom up appproach. Lets look at the optimal substructure.
##Since we have two strings, there is no way this ques can be done by a linear arr
##so we have to take a memo grid of n*m, so obviously that will be the complexity.
##Recursive formula is L[i][j] means number of times 1....i characters of s appears in 1...j characters of t
## L[i][j] = 0 if j=0 (obviously) L[i][j] = 1 if i=0 because that means number of times no character of s appears in t and that is at min 1

def FindCount():
    s = raw_input()
    t = raw_input()
    m = len(s)
    n = len(t)
    L = [[0]*(n+1) for i in range(m+1)]
    for i in range(n+1):
        L[0][i] = 1
    for i in range(m+1):
        L[i][0] = 0
    L[0][0] = 1

    for i in range(1,m+1):
        for j in range(1,n+1):
            
            if s[i-1]==t[j-1]:
                L[i][j] = L[i-1][j-1]+L[i][j-1]
            else:
                L[i][j] = L[i-1][j]
    print L            
    return L[m][n]


print FindCount()
