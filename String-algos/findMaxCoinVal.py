a = map(int,raw_input().split())
inclx = a[0]
exclx = 0
ma = inclx
for i in range(1,len(a)):
    temp  = inclx
    inclx = exclx+a[i]
    exclx = temp

ma = max(inclx,exclx)
print ma
