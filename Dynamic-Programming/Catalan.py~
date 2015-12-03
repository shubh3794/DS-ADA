##given n. You have 1...n nodes. Find out how many BST's can be formed with height less than or equal to h. And then sum the root nodes of all those BST's (Was asked in hackerearth, cleared 3/10 test cases).


x = map(int,raw_input().split())
s = x[0]
d = x[1]
a = [[None]*(500+1) for i in range(500+1)]

## this is function to calculate number of BST's with height less than or equal to h, based on the recurrence B(h,n) = B(h-1,i-1)*B(h-1,n-i)
def B(h,n):
    if h==0 and n==1:
        return 1
    if h>=0 and n==0:
        return 1
    if h ==0 and n>1:
        return 0
    if a[n][h]!=None:
        return a[n][h]
    sumi = 0
    for i in range(1,n+1):
        if a[i-1][h-1]!=None:
            k = a[i-1][h-1]
        else:
            k = B(h-1,i-1)
        if a[n-i][h-1]!=None:
            q = a[n-i][h-1]
        else:
            q = B(h-1,n-i)
        sumi += k*q
    a[n][h]=sumi
    return sumi

##this is the function to calculate sum
def summt(n,h):
    summi = 0
    for i in range(1,n+1):
        summi += i*B(h-1,i-1)*B(h-1,n-i)
    return summi

print B(s,d)
print summt(s,d)

