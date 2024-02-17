from typing import List 

class WordSearch:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, 0, i, j): return True
        return False

    def dfs(self, board: List[List[str]], word: str, idx: int, i: int, j: int) -> bool:
        if len(word) == idx: return True

        if (i < 0 or i >= len(board)    or 
            j < 0 or j >= len(board[0]) or 
            board[i][j] != word[idx]    or 
            board[i][j] == "#"):
            return False

        board[i][j] = "#" 
           
        if (self.dfs(board, word, idx+1, i + 1, j) or 
           self.dfs(board, word, idx+1, i - 1, j)  or 
           self.dfs(board, word, idx+1, i, j - 1)  or 
           self.dfs(board, word, idx+1, i, j + 1)):
            return True

        board[i][j] = word[idx]

        return False

        
