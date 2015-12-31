##Commonly used methods
a = [1,2,3,4,5,6,7]
def BinarySearch(x,lo,hi):
    if lo==hi:
        return lo
    
    elif lo<hi:
        mid = (lo+hi)/2
        if x< a[mid]:
            hi = mid-1
        else:
            lo = mid+1
        return BinarySearch(x,lo,hi)
    
print BinarySearch(3,0,len(a)-1)
        
