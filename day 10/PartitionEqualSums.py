class Solution:
    def canPartition(self, nums) -> bool:
        s = sum(nums)
        if s% 2 != 0 : return False
        dp = [0] * (s // 2 + 1)
        dp[0] = 1

        for num in nums :
            for i in range(s //2 ,-1,-1):
                if dp[i] == 1 and i + num <= s // 2:
                    dp[i + num] = 1 
        
        return dp[s//2] == True
