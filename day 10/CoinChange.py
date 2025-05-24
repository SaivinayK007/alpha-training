class Solution:
    def coinChange(self, coins ,amount: int) -> int:
        if amount == 0 : return amount
        
        cc = [1000000] *(amount + 1)
        cc[0] = 0 

        for amt in range(amount+1):
            for i in range(len(coins)):
                if coins[i] <= amt : 
                    cc[amt] = min(cc[amt] ,1 + cc[amt - coins[i]])
                    
        if cc[amount] == 1000000 : return -1
        return cc[amount]

'''
 Time Complexity : O(Len(coins) * Amount)

'''

class MemoSol:
    def __init__(self):
        self.memo = []

    def solve(self, coins,rem):
        if rem == 0 : return 0
        if rem < 0 : return float('inf')
        if self.memo[rem] != -1: return self.memo[rem]

    
        
    def coinChange (self, coins , amount):
        self.memo = [-1] *(amount + 1)
        res = self.solve(coins,amount)
        return -1 if res == float('inf') else res
        
        