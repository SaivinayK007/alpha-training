# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.node = None
        self.count = 0
        #Empty BST 
    def helper(self,preorder,bound):
        if self.count < len(preorder) and preorder[self.count] < bound:
            data = preorder[self.count]
            node = TreeNode(data)
            self.count +=1
            node.left = self.helper(preorder,data)
            node.right = self.helper(preorder,bound)

            return node
        else: return None

    def bstFromPreorder(self, preorder):
        return self.helper(preorder,float('inf'))


        