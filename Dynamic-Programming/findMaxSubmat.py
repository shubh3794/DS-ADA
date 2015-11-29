##given a matrix, find max submatrix with all 1's

def findMax():
    row = int(raw_input())
    col = int(raw_input())
    a = []
    for i in range(row):
        a.append(map(int,raw_input().split()))
    b =[[0]*col for i in range(row)]
    for i in range(row):
        b[i][0] = a[i][0]
    for j in range(col):
        b[0][j] = a[0][j]
    maxs= 0
    maxi= 0
    maxj = 0
    for i in range(1,row):
        for j in range(1,col):
            if a[i][j]:
                b[i][j] = min(b[i][j-1],b[i-1][j],b[i-1][j-1])+1
                if b[i][j]>maxs:
                    maxs = b[i][j]
                    maxi = i
                    maxj = j
            else:
                b[i][j] = 0
    for i in range(maxi - maxs + 1 , maxi+1):
        print "\n"
        for j in range(maxj - maxs + 1 , maxj+1):
            print a[i][j],

findMax()
                
