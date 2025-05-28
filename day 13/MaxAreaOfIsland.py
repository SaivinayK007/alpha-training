from typing import List

class Solution:
    def __init__(self):
        self.rows = 0
        self.cols = 0
    
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= self.rows or j >= self.cols or grid[i][j] == 0:
            return 0
        grid[i][j] = 0
        area = 1
        area += self.dfs(grid, i - 1, j)
        area += self.dfs(grid, i + 1, j)
        area += self.dfs(grid, i, j - 1)
        area += self.dfs(grid, i, j + 1)
        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.rows, self.cols = len(grid), len(grid[0])
        max_area = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.dfs(grid, i, j))
        return max_area
