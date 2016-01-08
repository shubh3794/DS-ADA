##Knuth Morris Pratt for string matching
a = raw_input()
b = raw_input()
def pattern(b):
    F = [None]*len(b)
    F[0]=0
    i = 1
    j = 0
    m = len(b)
    while i<m:
        if b[j]==b[i]:
            F[i] = F[j]+1
            i += 1
            j += 1
        elif j>0:
            j = F[j-1]
        else:
            F[i]=0
            i += 1
    return F

def match(a,b):
    F = pattern(b)
    i=0
    j=0
    m = len(b)
    n = len(a)
    while i<n:
        if a[i]==b[j]:
            if j==m-1:
                return i-j
            else:
                i += 1
                j += 1
        elif j>0:
            j = F[j-1]
        else:
            i += 1

print match(a,b)
