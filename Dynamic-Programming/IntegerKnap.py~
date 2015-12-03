##PROGRAM TO FILL A KNAPSACK WITH N TYPE OF ITEMS. THERE CAN BE INFINITE NUMBER OF EACH ITEMS AND BAG HAS A CAPACITY OF C. EACH TYPE OF OBJECT HAS A SIZE AND A VALUE. fILL THE BAG IN SUCH A WAY THAT VALUE OF BAG IS MAXIMUM. DUPLICATES ALLOWED

##BOTTOM UP APPROACH

def knap(a,s,c,M):
    M[0] = 0
    for i in range(1,c+1):
        temp = 0
        M[i]=M[i-1]
        for j in range(len(a)):
            if i>=s[j]:
                var = M[i-s[j]]+a[j]
                if var > temp:
                    temp = var
        
                if M[i] < temp:
                    M[i] = temp
       
    print M
    return M[c]

##TopBottom Approach
def knapa(a,s,c,M):
    if c<=0:
        return 0
    if M[c] != None:
        return M[c]
    temp = 0
    
    for j in range(len(a)):
        if c >= s[j]:
            var = knapa(a,s,c-s[j],M)+a[j]
            if var>temp:
                temp = var
    M[c]= knapa(a,s,c-1,M)
    if M[c]<temp:
        M[c]=temp
    return M[c]

a = [30,14,16,9]
c = 10
s = [6,3,4,2]
M = [None]*(c+1)
M[0]=0
print knapa(a,s,c,M)

