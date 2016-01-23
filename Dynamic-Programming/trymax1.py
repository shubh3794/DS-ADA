a =  map(int,raw_input().split())
##Count total number of 0's and 1's in the array
GC0 = 0
GC1 = 0
for i in range(len(a)):
    if a[i]==0:
        GC0 +=1
    else:
        GC1 += 1


if count1<len(a) and count0<len(a):
    L=0
    R=1
    count0=0
    count1=0
    if a[L]==0:
        count0 = 1
    else:
        count1 = 1
    bestL = -1
    bestR = -1
    max = 0
    while R<len(a):
        if a[R]==1:
            if count1<GC0:
                count1+=1
                R+=1
            else:
                if a[L]==1:
                    count1-=1
                L+=1
        else:
            if count0<GC1:
                count0+=1
                R+=1
            else:
                if a[L]==0:
                    count0-=1
                L+=1
        if R-L>max and count1==count0:
            max=R-L
            bestL=L
            bestR=R

    print bestL,bestR-1,max
else:
    print 'None'
