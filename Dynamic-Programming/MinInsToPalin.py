##Minimum number of insertions to a string to make it a plaindrome
##Top-bottom
def Ins(a,lo,hi,m):
    if lo==hi:
        m[lo][hi] = 0
        return m[lo][hi]
    if lo == hi-1:
        if a[lo]==a[hi]:
             m[lo][hi] = 0
        else:
            m[lo][hi] = 1
        return m[lo][hi]
    if m[lo][hi] != 0:
        return m[lo][hi]
    if a[hi]==a[lo]:
        m[lo][hi] = Ins(a,lo+1,hi-1,m)
    else:
        m[lo][hi] = min(Ins(a,lo,hi-1,m),Ins(a,lo+1,hi,m))+1
    return m[lo][hi]


def Insert():
    a = list(raw_input())
    n = len(a)
    m = [[0]*len(a) for i in range(len(a))]
    print 'top-bottom', Ins(a,0,len(a)-1,m)
    m = [[0]*len(a) for i in range(len(a))]
    for gap in range(1,n):
        for i in range(n-gap):
            j = i + gap
            if i == j-1:
                if a[i]==a[j]:
                    m[i][j] = 0
                else:
                    m[i][j] = 1
            elif a[i]==a[j]:
                m[i][j] = m[i+1][j-1]
            else:
                m[i][j] = min(m[i+1][j],m[i][j-1])+1
    print 'bottom up', m[0][n-1]
                
    
Insert()
