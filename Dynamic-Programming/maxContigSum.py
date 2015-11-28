## PROGRAM TO FIND THE SUBSET OF CONTIGUOUS ELEMENTS SUCH THAT SUM OF THOSE ELEMENTS IS MAXM

##DP APPROACH
def FindMaxSum(a):
    
    M = [None]*len(a)
    if a[0] <= 0 :
        M[0] = 0
    else:
        M[0] = a[0]
    maxi = M[0]
    for i in range(1,len(a)):
        if M[i-1]+a[i]<=0:
            M[i]=0
        else:
            M[i] = M[i-1]+a[i]
            if maxi < M[i]:
                maxi = M[i]
    return maxi

##Non Dp Approach

def FindSumMax(a):
    sumsofar = 0
    sumtillend = 0
    for i in range(len(a)):
        if sumtillend + a[i] > 0:
            sumtillend += a[i]
            if sumtillend>sumsofar:
                sumsofar=sumtillend
        else:
            sumtillend = 0
    return sumsofar

print FindMaxSum([-3,6,8,9-10,22,-1])
print "\n Huurah next method \n"
print FindSumMax([-3,6,8,9-10,22,-1])

