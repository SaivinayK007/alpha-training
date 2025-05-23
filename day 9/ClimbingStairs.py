class Solution:
    #Tabulation
    def climbStairs(self, n: int) -> int:
        if n <=2 : return n
        dp = [0] * (n+1)
        
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2

        for i in range(3 , n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
    
    '''
    Time Complexity:O(n)
    Space Complexity:O(n)
    '''
    
    #Optimised Space 0(1)
    def ClimbStairs(self , n):
        if n <= 2: return n
        a , b , c= 1,2,0
        for i in range(3 , n+1):
            c = a+b
            a , b = b , c
        return c
    
    
    '''
    Time Complexity:O(n)
    Space Complexity:O(1)
    '''

    #Memoization

    def func(self ,n):
        if n<=2 : return 
        return self.func(n-1) + self.func(n-2)
    
    


    