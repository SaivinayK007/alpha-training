# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init(self):
        self.root = None
    
    def findMax(self,root):
        while  root.right : root = root.right
        return root
    
    def deleteNode(self, root, key: int):
            if not root : return root
            if root.val > key : root.left = self.deleteNode(root.left , key)
            elif root.val < key : root.right = self.deleteNode(root.right,key)
            
            else:
                if not root.left : return root.right
                elif not root.right: return root.left

                max_Node = self.findMax(root.left)
                root.val = max_Node.val
                root.left = self.deleteNode(root.left ,max_Node.val)

            return root

        