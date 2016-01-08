##FINITE STRING AUTOMATA
a = raw_input()
b = raw_input()

def nextState(q,x):
    if q<len(b) and b[q]==x:
        return q+1
    else:
        i = 0
        for s in range(q,0,-1):
            if b[s-1]==x:
                for i in range(0,s-1):
                    if b[i]!=b[q-s+1+i]:
                        break
                if i==s-1:
                    return s
        return 0

def fillAutomata(b):
    number = ['a','b','c']
    stateTable = [[0]*3 for j in range(len(b)+1)]
    for i in range(len(b)+1):
        for j in range(3):
            temp = nextState(i,number[j])
            stateTable[i][j] = temp
    return stateTable

def search(a,b):
    table = fillAutomata(b)
    state = 0
    for i in range(len(a)):
        state = table[state][ord(a[i])-97]
        if state==len(b):
            return i-len(b)+1

print 'elem found at', search(a,b)
                             
    
    
    
