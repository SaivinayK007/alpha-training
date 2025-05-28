class Solution:
    def islandPerimeter(self, grid) -> int:
        rows , cols = len(grid) , len(grid[0])
        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    if i == 0 or grid[i-1][j] == 0 : count +=1
                    if j == 0 or grid[i][j-1] == 0 : count +=1
                    if i == rows - 1 or grid[i+1][j] == 0: count +=1
                    if j == cols - 1 or grid[i][j+1] == 0 : count +=1
        return count


        