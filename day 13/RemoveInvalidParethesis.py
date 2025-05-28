from typing import List

class Solution:
    def __init__(self):
        self.ans = []

    def backtrack(self, s, i, j, temp):
        bal = 0
        for k in range(i, len(s)):
            if s[k] == temp[0]:
                bal += 1
            elif s[k] == temp[1]:
                bal -= 1

            if bal < 0:
                for x in range(j, k + 1):
                    if s[x] == temp[1] and (x == j or s[x] != s[x - 1]):
                        self.backtrack(s[:x] + s[x + 1:], k, x, temp)
                return  

        s = s[::-1]
        if temp[0] == '(':
            self.backtrack(s, 0, 0, [')', '('])
        else:
            if s not in self.ans:
                self.ans.append(s)

    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.ans = []
        self.backtrack(s, 0, 0, ['(', ')'])
        return self.ans
