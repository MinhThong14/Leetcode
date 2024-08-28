class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        l, r = 0, 1
        max_len = 1
        
        cur_str = ""
        
        while r < n:
            cur_str = s[l:r]
            max_len = max(max_len, len(cur_str))
            while l < r and s[r] in cur_str:
                l += 1
                cur_str = s[l:r]

            r += 1
            
        max_len = max(max_len, r-l)
        
        return max_len
            
            
            