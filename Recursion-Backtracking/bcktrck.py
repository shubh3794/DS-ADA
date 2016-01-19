n = int(raw_input())
aux = [None]*2*n
def place(aux,ind):
    if None not in aux:
        print aux
        return
    if ind<=n:
        for i in range((2*n)-1-ind):
            temp = aux[i]
            temp2 = aux[i+ind+1]
            if aux[i]==None and aux[i+1+ind]==None:
                aux[i]=ind
                aux[1+i+ind]=ind
                place(aux,ind+1)
            aux[i]=temp
            aux[i+ind+1]=temp2

for i in range(n):
    temp = aux
    place(aux,i+1)
    aux = temp
