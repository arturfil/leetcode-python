from typing import List

class NumberOfIslands:
    def num_is_islands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j] == "1"):
                    count += 1
                    self.dfs(grid, i, j)
        
        return count

    def dfs(self, grid:List[List[str]], row:int, col:int) -> None:
        if grid[row][col] == "0": return
        grid[row][col] = "0"
        
        if row < len(grid)-1:  self.dfs(grid, row + 1, col)
        if row > 0: self.dfs(grid, row - 1, col)
        if col < len(grid[row])-1: self.dfs(grid, row, col+1)
        if col > 0: self.dfs(grid, row, col-1)

    def bfs(self, grid: List[List[int]], row:int, col:int) -> None:
        queue, directions = [[row, col]], [[1,0], [-1, 0], [0, 1], [0, -1]] # down, up, right, left
        
        while queue:
            for x in queue:
                [row, col] = queue.pop(0)
                for dir in directions:
                    new_row, new_col = row + dir[0], col + dir[1]
                    if new_row >= len(grid) or new_row < 0: continue
                    if new_col >= len(grid[new_row]) or new_col < 0: continue
                    if grid[new_row][new_col] == "0": continue
                        
                    grid[new_row][new_col] = "0"
                    queue.append([new_row, new_col])

