# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        # code here
        if not root : return []
        columns = dict()
        queue = [(root , 0)]
        max_col , min_col = 0 ,0 
        
        while queue:
            node , col = queue[0]
            queue.remove((node , col))
            
            if col not in columns :
                columns[col] = node.data
                
            min_col = min(min_col , col)
            max_col = max(max_col , col)
            
            if node.left : queue.append((node.left ,col - 1))
            if node.right : queue.append((node.right , col +1 ))
            
        ans = []
            
        for cols in range(min_col , max_col+1):
            if cols in columns:
                ans.append(columns[cols])
        return ans
if __name__ == "main":
    sol = Solution()
    sol.topView()

'''
Time Complexity: O(N)
''' 