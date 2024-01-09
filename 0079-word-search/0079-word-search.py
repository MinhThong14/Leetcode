class Solution:
    
    def dfs(self, i, j, board, word):
        if len(word) == 0:
            return True
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        
        if board[i][j] == word[0]:
            board[i][j] = '#'
            
            if self.dfs(i-1, j, board, word[1:]) or self.dfs(i+1, j, board, word[1:]) or self.dfs(i, j-1, board, word[1:]) or self.dfs(i, j+1, board, word[1:]):
                return True
            
            board[i][j] = word[0]
        
        return False
    
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        for i in range(m):
            for j in range(n):
                if self.dfs(i, j, board, word):
                    return True
        
        return False