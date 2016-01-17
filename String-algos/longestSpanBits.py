a = map(int,raw_input().split())
b = map(int,raw_input().split())
wl = 0
wr = 1
bestL=0
bestR=0
sum1 = a[wl]
sum2 = b[wl]
maxlen = 0
n = len(a)
while wl<n:
    if sum1+a[wr]!=sum2+b[wr]:
        sum1 = sum1 - a[wl]
        sum2 = sum2 - b[wl]
        wl += 1
        
    else:
        sum1 = sum1 + a[wr]
        sum2 = sum2 + b[wr]
        if wr-wl+1>maxlen:
            bestL=wl
            bestR=wr
        wr+=1
    
    
        
print bestL,bestR
