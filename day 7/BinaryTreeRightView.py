# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root :
            return []
        queue = [root] 
        res = []

        while len(queue) != 0:
            size = len(queue)
            

            for i  in range(size):
                top = queue[0]
                queue.remove(top)

                if i == size -1 : res.append(top.val)
                if top.left : queue.append(top.left)
                if top.right : queue.append(top.right)
            
            
        return res


        
'''
  Time Complexity : O(n)
'''