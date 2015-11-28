#Coin change: Given an array of coins, and a sum. Divide the amount into min num of coins
a = map(int,raw_input().split())
c = int(raw_input())
def CoinChange(a,c):
    m = len(a)
    coins = [None]*(c+1)
    coins[0] = 0
    for i in range(1,c+1):
        for j in range(m):
            if i-a[j]>=0:
                temp = coins[i-a[j]]+1
                if temp < coins[i]:
                    coins[i] = temp
    return coins[c]


print CoinChange(a,c)
    
