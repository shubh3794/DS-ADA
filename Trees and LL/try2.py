t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    a = map(int,raw_input().split())
    i=0
    j=n-1
    max = 2000000000
    min = 0
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
            if a[j]-a[i] < j-i-1:
                if a[j]-j < 0:
                    a[j] = max
                    max -= 1
                    j -= 1
                    
                else:
                    a[i] = min
                    min += 1
                    i += 1
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
