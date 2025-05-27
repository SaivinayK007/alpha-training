class Solution:
    def __init__(self):
        self.ans = []
    def dfs(self,n,left ,right ,s):
        if len(s) == 2*n : self.ans.append(s)
        if left < n : self.dfs(n,left +1 , right,s+'(')
        if right < left : self.dfs(n ,left,right +1 ,s+')')

    def generateParenthesis(self, n: int):
        self.dfs(n,0,0,"")
        return self.ans
        
        