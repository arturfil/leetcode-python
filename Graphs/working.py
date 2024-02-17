from typing import List

class NumberOfIslands:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1" :
                    res += 1
                    self.dfs(grid, row, col)

        return res

    def dfs(self, grid, row, col) -> None:
        if grid[row][col] == "0": return

        grid[row][col] = "0" # marking the one as visited

        if row < len(grid)-1: self.dfs(grid, row+1, col) # going downwards in the grid
        if row > 0: self.dfs(grid, row-1, col) # going upwards
        if col < len(grid[0])-1: self.dfs(grid, row, col + 1) # left
        if col > 0: self.dfs(grid, row, col - 1) # right
    
