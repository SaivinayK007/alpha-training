#User function Template for python3

class Solution:
    def bottomView(self, root):
        # code here
        columns = dict()
        queue = [(root , 0 )]
        
        min_col = max_col = 0
        
        while queue :
            node , col = queue[0]
            queue.remove((node ,col))
            
            columns[col] = node.data
            
            min_col = min(min_col , col)
            max_col = max(max_col , col)
            
            if node.left: queue.append((node.left , col - 1))
            if node.right : queue.append ((node.right , col + 1))
        ans = []
        
        for cols in range(min_col , max_col + 1):
            if cols in columns :
                ans.append(columns[cols])
        return ans


'''
  Time complexity :- O(N)
'''