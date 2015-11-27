##Subset sum problem- Find all the subsets in an array which is given such that sum of elements in a subset is k

def SubsetSum():
    a = map(int,raw_input().split())
    c = int(raw_input())
    m = [[False]*(len(a)+1) for i in range(c+1)]
    
    for i in range(len(a)+1):
        m[0][i] = True
    for i in range(1,c+1):
        for j in range(1,len(a)+1):
            if i-a[j-1]>=0:
                m[i][j] = m[i][j-1] or m[i-a[j-1]][j-1]
            else:
                m[i][j] = m[i][j-1]
    
    return m[c][len(a)]                      
print SubsetSum()
