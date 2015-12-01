##Find max sum subsequence such that the terms included in the sum are appearing in increasing order in array
##for example 1 2 90 4 5 89 6 has max sum as 101 because 1 + 2 + 4 + 5 + 89 = 101
##and that is an increasing subsequance

def maxSumSubSeq():
    a = map(int,raw_input().split())
    m = [0]*(len(a))
    m[0] = a[0]
    n =len(a)
    for i in range(1,n):
        for j in range(0,i):
            if a[j] < a[i]:
                q = m[j] + a[i]
                if q > m[i]:
                    m[i] = q
    print m
    return max(m)

print maxSumSubSeq()
