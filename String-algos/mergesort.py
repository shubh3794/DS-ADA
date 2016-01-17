a = map(int,raw_input().split())
def ms(a):
    aux = [None]*len(a)
    return sort(0,len(a)-1,aux,a)

def sort(lo,hi,aux,a):
    inv = 0
    if lo>=hi:
        return inv
    mid = (lo+hi)/2
    inv = sort(lo,mid,aux,a)
    inv += sort(mid+1,hi,aux,a)
    inv += merge(lo,hi,aux,a)
    return inv

def merge(lo,hi,aux,a):
    for i in range(lo,hi+1):
        aux[i]=a[i]
    i = lo
    mid = (lo+hi)/2
    j = mid+1
    k = lo
    inversions = 0
    while k<=hi:
        if i>mid and j<=hi:
            a[k]=aux[j]
            k+=1
            j+=1
        elif i<=mid and j>hi:
            a[k]=aux[i]
            i+=1
            k+=1
        elif aux[i]<=aux[j]:
            a[k]=aux[i]
            k+=1
            i+=1
        elif aux[j]<aux[i]:
            a[k]=aux[j]
            j+=1
            k+=1
            inversions += mid+1-i
    return inversions

print ms(a)
print a
