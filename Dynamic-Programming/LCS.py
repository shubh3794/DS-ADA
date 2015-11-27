#LCS(LONGEST COMMON SUBSEQUENCE) and SCS(shortest common bla bla)


##Function to traceback the common sequence
def printLCS(s,cnt,i,j,x):
    if cnt == 0:
        print "\n"
        return
    if s[i][j] == '\\':
        print x[i],
        printLCS(s,cnt-1,i+1,j+1,x)   
    elif s[i][j] =='|':
        printLCS(s,cnt,i+1,j,x)
    else:
        printLCS(s,cnt,i,j+1,x)


##function to identify the common sequence and count the length
def LCS():
    x = raw_input()
    y = raw_input()
    m = len(x)
    n = len(y)
    memo = [[0]*(n+1) for i in range(m+1)] ##Array to memoize
    s = [[0]*(n+1) for i in range(m+1)] ##array for traceback
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            if x[i]==y[j]:
                memo[i][j] = 1 + memo[i+1][j+1]
                s[i][j] = '\\'
            elif memo[i+1][j]>memo[i][j+1]:
                memo[i][j] = memo[i+1][j]
                s[i][j] = '|'
            else:
                memo[i][j] = memo[i][j+1]
                s[i][j] = '-'
    print "Longest common bla bla is \n"
    printLCS(s,memo[0][0],0,0,x)
    print memo[0][0]
    print "Shortest common bla bla is \n"
    SCS(x,y,m,n)
    


def SCS(x,y,m,n):
    memo = [[0]*(n+1) for i in range(m+1)] ##array for traceback
    s = [[0]*(n+1) for i in range(m+1)] ##array for traceback
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            if x[i]==y[j]:
                memo[i][j] = 1 + memo[i+1][j+1]
                s[i][j] = '\\'
            elif memo[i+1][j] < memo[i][j+1]:
                memo[i][j] = memo[i+1][j]
                s[i][j] = '|'
            else:
                memo[i][j] = memo[i][j+1]
                s[i][j] = '-'
    printLCS(s,memo[0][0],0,0,x)
    print memo[0][0]
    
LCS()
