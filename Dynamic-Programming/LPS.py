##LONGEST PALINDROMIC SUBSEQUENCE: find the longest sequence which is palindrome in a given string

##Top bottom approach is easier in this problem so lets first do that. Memoization is used


def TopBotLPS(i,j,L,a):
    if L[i][j] != 0:
        return L[i][j]
    if i==j:
        L[i][j]=1
        return 1
    if i == j-1 and a[i]==a[j]:
        L[i][j]=2
        return L[i][j]
    if a[i]==a[j]:
        L[i][j] = 2 + TopBotLPS(i+1,j-1,L,a)
        return L[i][j]
    if a[i]!=a[j]:
        L[i][j] = max(TopBotLPS(i+1,j,L,a),TopBotLPS(i,j-1,L,a))
        return L[i][j]
    
def BotUpLPS(a):
    x =len(a)
    L = [[0]*x for i in range(x)]
    for i in range(x-1):
        L[i][i]=1
        if a[i]==a[i+1]:
            L[i][i+1]=2
    L[x-1][x-1]=1

    for i in range(2,x+1):
        for j in range(0,x-i+1):
            k = j+i-1
            if a[j]==a[k]:
                L[j][k] = 2 + L[j+1][k-1]
            else:
                L[j][k] = max(L[j+1][k],L[j][k-1])
    return L[0][n-1]
                            
def findLPSTB():
    a = raw_input()
    print "Top-bottom-approach",
    L = [[0]*len(a) for i in range(len(a))]
    print TopBotLPS(0,len(a)-1,L,a)
    print "Bottom-up-approach",
    print BotUpLPS(a)
    

findLPSTB()
