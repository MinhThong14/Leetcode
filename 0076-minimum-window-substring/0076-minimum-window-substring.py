class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        t_dict = Counter(t)
        word_chr = {}
        
        l, r = 0, 0
        
        ans = (float('inf'), None, None)
        
        formed = 0
        
        while r < len(s):
            cur_char = s[r]
            
            if cur_char not in word_chr:
                word_chr[cur_char] = 0
            
            word_chr[cur_char] += 1
            
            if cur_char in t_dict and word_chr[cur_char] == t_dict[cur_char]:
                formed += 1
            
            while l <= r and formed == len(t_dict):
                
                char = s[l]
                
                if r - l + 1 < ans[0]:
                    ans = (r-l+1, l, r)
                
                word_chr[char] -= 1
                if char in t_dict and word_chr[char] < t_dict[char]:
                    formed -= 1   
                
                l += 1
            
            r += 1
        return "" if ans[0] == float('inf') else s[ans[1]:ans[2]+1]
             
            