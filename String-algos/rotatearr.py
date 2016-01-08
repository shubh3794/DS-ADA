##Rotate rray

def reverse(a,start,end):
    while start<end:
        a[start] = a[start]^a[end]
        a[end] = a[start]^a[end]
        a[start] = a[start]^a[end]
        end -= 1
        start += 1

def rotate(a,d):
    reverse(a,0,d-1)
    reverse(a,d,len(a)-1)
    reverse(a,0,len(a)-1)
    return a

a = map(int,raw_input().split())
d = int(raw_input())
print rotate(a,d)
