a = map(int,raw_input().split())
i = map(int,raw_input().split())
for j in range(len(a)):
    temp = a[i[j]]
    a[i[j]] = a[j]
    a[j]=temp
    i[i[j]]=i[j]

print a
