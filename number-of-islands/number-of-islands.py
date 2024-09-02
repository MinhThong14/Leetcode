from collections import deque

class Solution:
    def bfs(self, grid, cur_point):
        queue = deque()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        m, n = len(grid), len(grid[0])
        
        queue.append(cur_point)
        
        while queue:
            x, y = queue.popleft()
            for i, j in directions:
                if x+i > -1 and x+i < m and y + j > -1 and y + j < n and grid[x+i][y+j] == "1":
                    grid[x+i][y+j] = "0"
                    queue.append((x+i, y+j))
        
        
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        num_islands = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    num_islands += 1
                    self.bfs(grid, (i, j))
                    
        return num_islands