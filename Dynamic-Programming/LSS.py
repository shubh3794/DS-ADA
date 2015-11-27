#LIS
a = map(int,raw_input().split())
m = [1]*len(a)
def LIS(index):
    if index==0:
        return m[0]
    if m[index] != 1:
        return m[index]
    for i in range(index-1,-1,-1):
        q = LIS(i)
        if a[i]<a[index] and m[index] < q+1:
            m[index] = q+1

    return m[i]
LIS(len(a)-1)
print m
