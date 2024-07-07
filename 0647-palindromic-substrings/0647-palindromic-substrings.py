class Solution:
    def expandArroundCenter(self, s, l, r):
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            count += 1
        
        return count
    
    def countSubstrings(self, s: str) -> int:
        
        res = 0
        
        for i in range(len(s)):
            res += self.expandArroundCenter(s, i, i)
            res += self.expandArroundCenter(s, i, i+1)
            
        return res
        