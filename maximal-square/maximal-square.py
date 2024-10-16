class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        r = len(matrix)
        c = len(matrix[0])
        # dp = [[0] * (c+1) for _ in range(r+1)]
        
        max_len = 0
        
#         for i in range(1, r + 1):
#             for j in range(1, c + 1):
#                 if matrix[i-1][j-1] == "1":
#                     dp[i][j] = (min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1)
                    
#                     max_len = max(max_len, dp[i][j])
        
#         return max_len * max_len
        dp = [0] * (c + 1)
        prev = 0
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                temp = dp[j]
                if matrix[i-1][j-1] == "1":
                    dp[j] = min(dp[j-1], dp[j], prev) + 1
                    max_len = max(max_len, dp[j])
                else:
                    dp[j] = 0
                
                prev = temp
        
        return max_len * max_len