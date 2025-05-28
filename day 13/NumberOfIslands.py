class Solution:

    def dfs(self,a,i,j):

        if i < 0 or j < 0 or i>=len(a) or j >= len(a[0]) or a[i][j] == '0': 
            return

        a[i][j] = '0'

        self.dfs(a,i-1,j)
        self.dfs(a,i,j-1)
        self.dfs(a ,i+1,j)
        self.dfs(a,i,j+1)

     
    def numIslands(self, grid) -> int:

        rows = len(grid)
        cols = len(grid[0])

        count = 0 

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count +=1
                    self.dfs(grid,i,j)

        return count




        