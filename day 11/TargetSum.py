class Solution:
    def findTargetSumWays(self, nums, target: int) -> int:
        total  = sum(nums)
        if (target + total) % 2 != 0 or abs(target) > total : return 0

        temp =(target + total) // 2
        dp = [0] * (temp + 1)
        dp[0] = 1

        for i in range(len(nums)):
            j = temp
            while j >= nums[i]:
                dp[j] += dp[j-nums[i]]
                j-=1
        return dp[temp]

