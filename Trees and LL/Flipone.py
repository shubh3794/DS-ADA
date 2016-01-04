##Find index to be flipped which will giv e max number of contig 1's in an array
a = map(int,raw_input().split())
left = 0
right = 0
mid = 0
max_diff = -1
index = None
for i in range(len(a)):
    if a[i]==1:
        right = i
        ln = right - left + 1
    elif a[i]==0:
        left = mid+1
        mid = i
        right = i
        ln = right - left + 1
    if ln>max_diff:
        max_diff = ln
        index = mid

print index,max_diff        
        
    
