##Number of ways to reach the end
n = int(raw_input())
m = [0]*(n+1)
m[n]=1
for i in range(n-1,-1,-1):
    if i+1<=n:
        m[i] += m[i+1]
    if i+2<=n:
        m[i] += m[i+2]
    if i+3<=n:
        m[i] += m[i+3]
print m[0]
