# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.root = None
        
    
    def function(self ,nums, low , high):
        if low > high : return
        mid = (low +  high)//2
        node = TreeNode(nums[mid])
        node.left = self.function(nums , low , mid -1)
        node.right = self.function(nums , mid + 1, high)

        return node
        
    def insert(self,root ,num):
        if not root : return TreeNode(num)
        if root.val >= num : root.left = self.insert(root.left,num)
        else: root.right = self.insert(root.right,num)
        return root
        
        
    def sortedArrayToBST(self, nums) :
        size = len(nums)
        self.function(nums, 0 , size - 1)
        return self.root
        

        