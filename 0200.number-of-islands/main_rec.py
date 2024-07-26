from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def dfs(grid: List[List[str]], i: int, j: int):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]):
                return
            if grid[i][j] == '0' or grid[i][j] == 'V':
                return
            if grid[i][j] == '1':
                grid[i][j] = 'V'
                dfs(grid, i+1, j)
                dfs(grid, i-1, j)
                dfs(grid, i, j+1)
                dfs(grid, i, j-1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1

        return count
