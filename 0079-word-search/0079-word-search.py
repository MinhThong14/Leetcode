class Solution:
    
    def dfs(self, board, word, i, j):
        if len(word) == 0:
            return True
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        
        if board[i][j] == word[0]:
            board[i][j] = '#'
            
            if self.dfs(board, word[1:], i+1, j) or self.dfs(board, word[1:], i-1, j) or self.dfs(board, word[1:], i, j+1) or self.dfs(board, word[1:], i, j-1):
                return True
            
            board[i][j] = word[0]
        
        return False
            
        
        
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, i, j):
                    return True
        
        return False