# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root, val: int) :
        newNode = TreeNode(val)

        if not root : return newNode 
        temp = root

        while True :
            if temp.val >= val:
                if not temp.left :
                    temp.left = newNode
                    break
                else:
                    temp = temp.left
            else:
                if not temp.right :
                    temp.right = newNode
                    break
                else:
                    temp = temp.right
        return root
        

    def recurInsertBST(self , root , val) :
        if not root : return TreeNode(val)
        elif root.val >= val : root.left = self.recurInsertBST(root.left , val)
        else : root.right = self.recurInsertBST(root.right , val)
        return root
    