##given a particular number of indexes that can be flipped and an array of 0 and 1
##find all indexes to be flipped to form max number of 1's in an array
a = map(int,raw_input().split())
m = int(raw_input())
L = 0
R = 0
best = 0
count = 0
bL = 0
while R<len(a):

    if a[R]==0:
        if count < m:
            count += 1
            R += 1
        else:
            L += 1
            count -= 1
    else:
        R += 1
    
        if R-L>best:
            best = R-L
            bL = L
for i in range(best):
    if a[bL+i]==0:
        print bL+i,
print '\n',best
        
