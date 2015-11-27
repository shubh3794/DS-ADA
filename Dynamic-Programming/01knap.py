##Given a bag of C kg capacity, and an array of size n containing value of some
##items. In another array, weight of the respective items are given. Find the maximum
##value that can be gathered in the bag. Items cannot be duplicated

##Bottom up approach
def knap01():
    a = map(int,raw_input().split()) ## value of items
    w = map(int,raw_input().split()) ##weight of items
    c = int(raw_input()) ##capacity
    m = [[0]*(len(a)+1) for i in range(c+1)]
    ##m[i][j] is max value that can be collected in bag os size i from the array a
    ##index limited to 1...j
    for i in range(1,c+1):
        for j in range(1,len(a)+1):
            m[i][j] = m[i][j-1]
            if i - w[j-1] >= 0:
                q = m[i-w[j-1]][j-1]+a[j-1]
                if q > m[i][j]:
                    m[i][j] = q
    return m[c][len(a)]

print knap01()


##Top bottom approach
def TopBot():
    c = int(raw_input()) ## capacity of bag
    w = map(int,raw_input().split())## weight of items
    v = map(int,raw_input().split()) ## value of items
    m = [[0]*(len(w)+1) for i in range(c+1)] ##m[i][j] is max value that can be collected in bag os size i from the array a
    ##index limited to 1...j
    knap(c,len(w))
def Knap(i,j):
    global v,m,w
    if i==0 or j==0:
        m[i][j]=0
        return m[i][j]
    if m[i][j] != 0:
        return m[i][j]
    else:
        a = Knap(i,j-1)
        if i-w[j-1]>=0:
            b = Knap(i-w[j-1],j-1)+v[j-1]
        else:
            b = -1
        q = max(a,b)
        if q > m[i][j]:
            m[i][j]=q
    return m[i][j]
