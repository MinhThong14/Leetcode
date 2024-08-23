class Solution:
    
    def dfs(self, grid, m, n, directions, row, col):
        if row < 0 or row == m or col < 0 or col == n or grid[row][col] == 0:
            return 0
        
        max_len = 0
        val = grid[row][col]
        grid[row][col] = 0
        
        for x, y in directions:
            max_len = max(self.dfs(grid, m, n, directions, row+x, col+y)+val, max_len)
        
        grid[row][col] = val
        return max_len
        
    
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        max_gold = 0
        
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                max_gold = max(max_gold, self.dfs(grid, m, n, directions, i, j))
        
        return max_gold
        