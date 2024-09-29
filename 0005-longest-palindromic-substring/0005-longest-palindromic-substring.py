class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        ans = (0, 0)
        
        for i in range(n):
            dp[i][i] = 1
            ans = (i, i)
        
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                ans = (i,i+1)
        
        for diff in range(2, n+1):
            
            for i in range(n-diff):
                j = i+diff
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = 1
                    ans = (i, j)
        
        i, j = ans[0], ans[1]
        return s[i:j+1]
                    
        
        