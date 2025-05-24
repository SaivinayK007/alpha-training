class Solution:

    def rob(self, nums) -> int:
        n = len(nums) 

        if n == 1: return nums[0]
        if n == 2 : return max(nums)

        dp= [0] *(n)
        maxi = 0 

        dp[0]  = nums[0]
        dp[1] = max(nums[0] ,nums[1])

        for i in range(2 , n - 1):
            dp[i] = max(dp[i-2] + nums[i] , dp[i-1])
        maxi = dp[-2]

        dp.clear()

        dp = [0] * n

        dp[0] = nums[1]
        dp[1] = max(nums[1] ,nums[2])

        for i in range(3 , n):
            dp[i-1] = max(dp[i-3] + nums[i] , dp[i-2])
        return max(maxi , dp[-2])
        

        '''
        TIme
        '''