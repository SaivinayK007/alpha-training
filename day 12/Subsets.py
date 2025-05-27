class Solution:
    def __init__(self):
        self.ans = []
    
    def dfs(self,nums,temp,i):
        self.ans.append(temp[:])
        for j in range(i,len(nums)):
            temp.append(nums[j])
            self.dfs(nums,temp,j+1)
            temp.pop()
        


    def subsets(self, nums):
        temp = list()
        self.dfs(nums,temp,0)
        return self.ans
    
#Without Recursion

def naiveApp(nums ):
    ans  = []
    ans.append([])

    for i in range(len(nums)):
        temp = len(ans)
        for j in range(temp):
            temp = ans[j][:]
            temp.append(nums[i])
            ans.append(temp)
    return ans

ans = naiveApp([1,2,3])
ans.sort()
print(ans)