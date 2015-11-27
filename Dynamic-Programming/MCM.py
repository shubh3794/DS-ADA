##optimal way of multiplying n matrices
import sys
a = map(int,raw_input().split())
##This would take n elemnts as array say 2,4,6,8,9,11
##which means we have n-1 matrices of size 2*4,4*6,6*8 and so on
n = len(a)-1
## m is the array which stores results, m[i][j] means min cost of multiplying ith matrix with jth matrix
m = [[sys.maxint]*n for i in range(n)]
for i in range(n):
    m[i][i]=0

def BottomUp():
    global a,n,m
    for l in range(2,n+1):
        for i in range(0,n-l+1):
            j = i+l-1
            for k in range(i,j):
                q = m[i][k] + m[k+1][j] + a[i]*a[k+1]*a[j+1]
                if q < m[i][j]:
                    m[i][j]=q
    return m[0][n-1]


def partition(start,end):
    if start==end:
        return 0
    if m[start][end] != sys.maxint:
        return m[start][end]
    for i in range(start,end):
        q = partition(start,i)+partition(i+1,end)+a[start]*a[i+1]*a[end+1]
        if q < m[start][end]:
            m[start][end] = q
    return m[start][end]


print BottomUp()
print "\n"
print 'by top bottom',partition(0,n-1)
