# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return []
        queue = [root] 
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
            
            res.append(temp)
        return res



        
'''
  Time Complexity : O(n)
'''