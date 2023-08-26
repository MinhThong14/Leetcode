class Solution:
    
    def bfs(self, grid, i, j):
        
        queue = [(i, j)]
        
        origins = [(0,1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            x, y = queue.pop(0)
            grid[x][y] = '*'
            for mov_x, mov_y in origins:
                next_x = x + mov_x
                next_y = y + mov_y
                if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]) and grid[next_x][next_y] == '1':
                    grid[next_x][next_y] = '*'
                    queue.append((next_x, next_y))

    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    self.bfs(grid, i, j)
        
        return res
                    
        
        