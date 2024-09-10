class Solution:
    
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        
        if not s or not t:
            return ""
        
        t_counter = Counter(t)
        
        s_char = {}
        
        l, r = 0 , 0
        
        ans = (float('inf'), l, r)
        
        formed = 0
        
        while r < m:
            cur_char = s[r]
            
            if cur_char not in s_char:
                s_char[cur_char] = 1
            else:
                s_char[cur_char] += 1
            
            
            if cur_char in t_counter and s_char[cur_char] == t_counter[cur_char]:
                formed += 1
            
            
            while l <= r and formed == len(t_counter):
                char = s[l]
                
                if r-l+1 < ans[0]:
                    ans = (r-l+1, l, r)
                
                s_char[char] -= 1
                
                if char in t_counter and s_char[char] < t_counter[char]:
                    formed -= 1
                
                l += 1      
            
            r += 1
        
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]
            
            
                
        
        
        
        
        