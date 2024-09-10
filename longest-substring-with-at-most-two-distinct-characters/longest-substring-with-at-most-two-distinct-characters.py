

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        m = len(s)
        
        l, r = 0, 0
        
        ans = float('-inf')
        
        num_char = 0
        
        chars = {}
        
        while r < m:
            cur_char = s[r]
            
            if cur_char not in chars:
                chars[cur_char] = 1
            else:
                chars[cur_char] += 1
            
            while l < r and len(chars) > 2:
                char = s[l]
                chars[char] -= 1
                
                if chars[char] == 0:
                    chars.pop(char)
                
                l += 1
                
            if r - l + 1 > ans:
                ans = r-l+1
                
            r += 1
        
        return ans
                
            
            
            
            