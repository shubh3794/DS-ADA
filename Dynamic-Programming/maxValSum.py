a = map(int,raw_input().split())
maxSum = 0
arrSum = 0
for i in range(len(a)):
    maxSum+= a[i]*i
    arrSum += a[i]
last = len(a)-1
currSum = maxSum
for i in range(1,len(a)):
    currSum -= a[last]*(len(a)-1)
    currSum += arrSum
    currSum -= a[last]
    if currSum>maxSum:
        maxSum=currSum
    last = last-1

print maxSum
    
