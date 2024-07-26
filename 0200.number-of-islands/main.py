from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def dfs(grid: List[List[str]], i: int, j: int):
            stack = []
            while stack:
                i, j = stack.pop()
                if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]):
                    continue
                if grid[i][j] == '0' or grid[i][j] == 'V':
                    continue
                grid[i][j] = 'V'
                stack.append((i+1, j))
                stack.append((i-1, j))
                stack.append((i, j+1))
                stack.append((i, j-1))

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1

        return count
