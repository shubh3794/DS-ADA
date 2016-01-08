a = [11,None,17,None,None,None,20]
b = [5,8,12,14]
i = 0
m = 3
n = 4
j = n
while i<j and j<m+n:
    if a[i]==None:
        i += 1
    elif a[i] !=None:
        if a[j] == None:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
        else:
            j += 1
i = 0
j = 0
small_a = n

while i < m+n and j<n:
    if b[j] < a[small_a]:
        a[i] = b[j]
        i += 1
        j += 1
    else:
        a[i] = a[small_a]
        a[small_a] = None
        small_a += 1
        i+= 1
print a

    
    
