def dicethrow(sum,turn,max_val):
    if turn==1 :
        if sum <= max_val:
            return 1
        else:
            return 0
    temp = 0
    for i in range(1,max_val+1):
        if i < sum:
            temp += dicethrow(sum-i,turn-1,max_val)          
    return temp
print dicethrow(8,3,6)
