##Given n. divide n such that product of the divided numbers so formed is max.
##for eg 6 has 1,2,3,4,5 as divisions so max product will be 3*3 = 9

def divide():
    x = int(raw_input())
    a = []
    for i in range(1,x):
        a.append(i)
    m = [1]*(x+1)
    for i in range(2,x+1):
        for j in range(0,x-1):
            if i - a[j] >=0:
                q = m[i-a[j]]*a[j]
                if q > m[i]:
                    m[i]=q
    return m[x]
print "max prodcut is" , divide()
