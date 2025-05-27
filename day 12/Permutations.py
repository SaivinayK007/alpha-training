class Solution:
    def __init__(self):
        self.ans = []
    
        def dfs(self ,nums , ind):
            if ind == len(nums):
                self.ans.append(nums[:])
                return

            for j in range(ind,len(nums)):
                nums[ind],nums[j] = nums[j] ,nums[ind]
                self.dfs(nums , ind +1)
                nums[ind] ,nums[j] = nums[j] , nums[ind]
        

        def permute(self, nums) :
            self.dfs(nums,0)
            return self.ans