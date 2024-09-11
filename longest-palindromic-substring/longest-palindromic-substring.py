class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        m = len(s)
        
        dp = [[False for _ in range(m)] for _ in range(m)]
        
        ans = [0, 0]
        
        for i in range(m):
            dp[i][i] = True
        
        for i in range(m-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans = [i, i+1]
        
        
        for diff in range(2, m):
            for i in range(m-diff):
                j = i + diff
                
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    ans = [i, j]
        i, j = ans
        
        return s[i:j+1]
        