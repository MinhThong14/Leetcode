class Solution:
       
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        @lru_cache(None)
        def dfs(r, c):
            ans = 1
            
            for i, j in DIR:
                nr, nc = r + i, c + j
                if nr < 0 or nr == m or nc < 0 or nc == n or matrix[nr][nc] <= matrix[r][c]:
                    continue
                
                ans = max(ans, dfs(nr, nc) + 1)
                
            return ans
            
        
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        
        return ans
                