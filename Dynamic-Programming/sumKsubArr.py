from collections import defaultdict
a = map(int,raw_input().split())
k = int(raw_input())
hash={}
sum = 0
for i in range(len(a)):
    sum+=a[i]
    hash[sum]=i

sum2 = 0

for i in range(len(a)):
    sum2+=a[i]
    if k-sum2==0:
        print "found at",0,i
    elif k+sum2 in hash and i+1<=hash[k+sum2]:
        print "subarr found at",i+1,hash[k+sum2]
