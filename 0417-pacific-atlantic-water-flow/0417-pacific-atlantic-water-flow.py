from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific_queue = deque()
        atlantic_queue = deque()
        
        m, n = len(heights), len(heights[0])
        
        for i in range(n):
            pacific_queue.append((0, i))
            atlantic_queue.append((m-1, i))
        
        for j in range(m):
            pacific_queue.append((j, 0))
            atlantic_queue.append((j, n-1))
        
        def bfs(queue):
            directions = [(0,1), (0, -1), (-1, 0), (1, 0)]
            reachable = set()
            while queue:
                i, j = queue.popleft()
                reachable.add((i, j))
                
                for x, y in directions:
                    next_i, next_j = i+x, j+y
                    
                    if 0 <= next_i < m and 0 <= next_j < n and not (next_i, next_j) in reachable and heights[i][j] <= heights[next_i][next_j]:
                        queue.append((next_i, next_j))
            
            return reachable
                
                    
        pacific_reachable = bfs(pacific_queue)
        print(f"pacific reachable: {pacific_reachable}")
        atlantic_reachable = bfs(atlantic_queue)
        
        return list(pacific_reachable.intersection(atlantic_reachable))
        
            