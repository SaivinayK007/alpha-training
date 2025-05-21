#User function Template for python3


'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing elements of left view of the binary tree.
class Solution:
    def LeftView(self, root):
        # code here
        if not root :
            return []
        queue = [root] 
        res = []

        while len(queue) != 0:
            size = len(queue)
            

            for i  in range(size):
                top = queue[0]
                queue.remove(top)

                if i == 0: res.append(top.data)
                if top.left : queue.append(top.left)
                if top.right : queue.append(top.right)
            
            
        return res
    

        
'''
  Time Complexity : O(n)
'''