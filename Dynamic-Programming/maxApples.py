##Given a grid of size n*m and in it, each cell has some number of apples, You are currently
##on 0,0 You have to reach n-1,m-1 such that you have collected maximum number of apples
def CollectMax():
    a = []
    rows = int(raw_input())
    col = int(raw_input())
    for i in range(rows):
        a.append(map(int,raw_input().split()))
    m = [[0]*col for i in range(rows)]
    m[0][0] = a[0][0]
    for i in range(rows):
        for j in range(col):
            if i!=0 or j!=0:
                if i-1>=0 and j-1>=0:
                    m[i][j] = max(m[i][j-1],m[i-1][j]) +a[i][j]
                elif i-1<0:
                    m[i][j] = m[i][j-1]+a[i][j]
                else:
                    m[i][j] = m[i-1][j]+a[i][j]
    return m[rows-1][col-1]

print CollectMax()
