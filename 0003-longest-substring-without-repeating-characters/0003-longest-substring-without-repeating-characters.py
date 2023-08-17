class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        max_length = 0
        
        while r <= len(s):
            substring = s[l:r]
            
            if r < len(s) and s[r] not in substring:
                substring += s[r]
            elif r < len(s):
                l += 1
                continue
            
            max_length = max(max_length, len(substring))
            r += 1
        return max_length
            
            