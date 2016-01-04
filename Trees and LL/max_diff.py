a = map(int,raw_input().split())
small = 0
max_diff = a[1]-a[0]
for i in range(2,len(a)):
    if a[i]-a[small]>=max_diff:
        diff = a[i]-a[small]
    elif a[i]<a[small]:
        small=i
        diff = a[i+1]-a[small]
        
    if diff > max_diff:
        max_diff = diff
print max_diff
