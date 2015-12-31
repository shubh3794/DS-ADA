n = int(raw_input())
a = map(int,raw_input().split())
i=0
j=n-1
max = 1000000000
min = 1
change = 0
while i<n and j >= 0 and i<=j:
    if j-i==1:
        if a[i] < a[j]:
            break
        else:
            a[i] = min
            change += 1
            break

    elif i != j:
##checks whether the current values of a[i] and a[j] can work bcz if   not then we would not be able to make the array sorted j-i-1 is the number of elements in between i and j
        if a[j]-a[i] < j-i or a[j]-a[i]<=0:
##check whether a[j]'s value is valid or not. It would not be valid if a[j]-j < 0 because then we would not be able to fill up all positions less that j with elements less than a[j]
            if a[j]-j < 1 or a[j]-a[i]<j-1:
                a[j] = max
                max -= 1
                min = a[i]+1
                if a[j]< a[j-1]:
                    a[j-1] = max
                    max -= 1
                    change += 1
                    j -= 1
                else:
                    j-= 1
                if a[i] > a[i+1]:
                    a[i+1] = min
                    min += 1
                    change += 1
                    i += 1

            else:
                a[i] = min
                min += 1
                max = a[j]-1
                if a[i] > a[i+1]:
                    a[i+1] = min
                    min += 1
                    change += 1
                    i += 1
                else:
                    j -= 1
                if a[j]< a[j-1]:
                    a[j-1] = max
                    max -= 1
                    change += 1
                    j -= 1
            change += 1
                
        else:
            min = a[i]+1
            max = a[j]-1

            if a[i] > a[i+1]:
                a[i+1] = min
                min += 1
                change += 1
                i += 1
            else:
                i += 1
            if a[j]< a[j-1]:
                a[j-1] = max
                max -= 1
                change += 1
                j -= 1

    else:
        if a[i] < a[i+1]:
            if a[i] < a[i-1]:
                a[i] = min
                change += 1
        else:
            a[i] = max
            change += 1


print change
print a
