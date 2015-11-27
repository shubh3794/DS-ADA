##OPTIMAL STRATEGY TO WIN A GAME(payU and Amazon and Narsimha): Given an array of coins, and two players, players play turn wise such that they have to pick a coin which at either end, and nowhere else, device an optimal strategy so that you would always win the game. Assume that you always start first. Display the maximum value obtained by you as a result of this strategy

class OptimalStrategy:
    def __init__(self):
        self.a = map(int,raw_input().split())
        self.len = len(self.a)
        self.memo = [[-1]*self.len for i in range(self.len)]
        for i in range(self.len):
            (self.memo)[i][i] = (self.a)[i]
        for i in range(self.len-1):
            if self.a[i]>=(self.a)[i+1]:
                (self.memo)[i][i+1] = (self.a)[i]
            else:
                (self.memo)[i][i+1] = (self.a)[i+1]
                
    def run(self,x):
        if x == 0:
            return self.BottomUp()
        else:
            return self.TopBottom(0,self.len-1)

    def BottomUp(self):
        for i in range(0,self.len-1):
            for j in range(i+2, self.len):
                self.memo[i][j] = max(min(self.memo[i+1][j-1],self.memo[i+2][j])+self.a[i], min(self.memo[i][j-2],self.memo[i+1][j-1])+self.a[j])
        return self.memo[0]
    def TopBottom(self,lo,hi):
        if lo==hi:
            return self.memo[lo][lo]
        if self.memo[lo][hi] != -1 or hi-lo==1:
            return self.memo[lo][hi]
        i = lo
        j = hi
        self.memo[lo][hi] = max(min(self.TopBottom(i+1,j-1),self.TopBottom(i+2,j))+self.a[i], min(self.TopBottom(i,j-2),self.TopBottom(i+1,j-1))+self.a[j])
        return self.memo[lo][hi]

test = OptimalStrategy()
print test.run(1)
        
        
    
            
                
            
                
