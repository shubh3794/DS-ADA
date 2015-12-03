##Amazon interview ques: fairly simple. Given n pairs each containing nums n1,n2 such that
##n1<=n2. find the maximum chain length that can be formed by these such that
##if p1,p2 are two pairs in chain then p[1]<=p[2].
##Example : if n==3 and pairs are (2,4); (1,6); (5,7) then answer is 2 because poss
#chain is (2,4), (5,7)

class inValid(Exception):
    """Raised when first item of provided pair is greater than the second"""
    pass

def findMaxChain():
    n = int(raw_input())
    a = []
    for i in range(n):
        try:
            x = map(int,raw_input().split())
            if x[0]>x[1]:
                raise inValid
            else:
                a.append(x)
        except inValid:
            print "first item is larger than second"
    m = [0]*n
    m[0]=1
    for i in range(1,n):
        for j in range(0,i):
            if a[i][0]>=a[j][1]:
                q = m[j]+1
                if q > m[i]:
                    m[i] = q

    return m
print findMaxChain()
