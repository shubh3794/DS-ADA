#EDIT DISTANCE : MIN COST TO TRANSFORM A STRING TO OTHER, You can replace, delete
##insert only and cost of each op is given by user
import sys
def EditDist():
    a = raw_input()
    b = raw_input()
    m = len(a)
    n = len(b)
    ci = int(raw_input())
    cd = int(raw_input())
    cr = int(raw_input())
    temp = [[sys.maxint]*(m+1) for i in range(n+1)] ##temp[i][j] is cost for converting 1..i characters of a to 1...j characters of b
    for i in range(n+1):
        for j in range(m+1):
            if i==0:
                temp[i][j]=j*ci ##if i=0, cost of converting 1..i to 1..j is j*cost of insertion. because i=0 means length=0
            elif j==0:
                temp[i][j]=i*cd ##if j=0, cost of converting 1..i to lengh 0 is i*cost of deletion. because j=0 means length=0
            elif b[i-1]==a[j-1]:
                temp[i][j]=temp[i-1][j-1]
            else:
                temp[i][j]=min(temp[i-1][j-1]+cr, temp[i][j-1]+ci,temp[i-1][j]+cd)
    return temp[n][m]

print EditDist()
        
