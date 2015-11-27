##Min number of jumps to reach from first to last element. Maximum length of jump at a time can be equal to the value at the index at which the cursor currently is: for example 2 3 5 1. Starting from first index, the first jump can be of maximum length 2
import sys
a = map(int,raw_input().split())
m = [sys.maxint]*len(a)
m[0] = 0
def reachEnd(a,m):
    for i in range(1,len(a)):
        for j in range(i):
            if a[j]>=i-j and m[i] > m[j]+1:
                m[i] = m[j]+1
    return m[len(m)-1]

print reachEnd(a,m)
