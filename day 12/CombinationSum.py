from typing import List

class Solution:
    def __init__(self):
        self.ans = [] 

    def dfs(self, a, target, i, temp):
        if target == 0:
            self.ans.append(temp.copy())  # Fix: use copy to avoid reference issues
            return
        if target < 0:
            return

        for j in range(i, len(a)):
            temp.append(a[j])
            self.dfs(a, target - a[j], j, temp)
            temp.pop()  # backtrack

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []  # Clear previous answers if reused
        self.dfs(candidates, target, 0, [])
        return self.ans
