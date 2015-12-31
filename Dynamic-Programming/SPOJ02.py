n = int(raw_input())
a = map(int,raw_input().split())
L = [0]*(n)
length = 0    
            
                 
def BS(x,length):
    lo = 0
    hi = length
    while lo<=hi:
        mid = (lo+hi)/2
        if L[mid]<=x:
            lo = mid+1
        else:
            hi = mid-1
    newL = lo
    L[newL] = x
    return newL

for i in range(len(a)):
    a[i] = a[i]-i
for i in range(len(a)):
    if a[i] >= 1:
        temp = BS(a[i],length)
        if temp > length:
            length = temp
        
print len(a)-(length)

            
            
                

