# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return []
        queue = [root] 
        level = 1
        res = []

        while len(queue) != 0:
            size = len(queue)
            temp = list()

            for _  in range(size):
                top = queue[0]
                queue.remove(top)

                temp.append(top.val)

                if top.left : queue.append(top.left)
                if top.right : queue.append(top.right)

            if level % 2 == 0 :
                temp = temp[::-1]
            res.append(temp)
            level +=1
            
        return res

            

        
'''
  Time Complexity : O(n)
'''