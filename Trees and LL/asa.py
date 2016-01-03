def findMaxK():
    n = int(raw_input())
    a = map(int,raw_input().split())
    k = int(raw_input())
    for i in range(0,n-k+1):
        max = a[i]
        for j in range(i,i+k):
            if a[j]>max:
                max = a[j]
        print max,
    return 0    


findMaxK()
