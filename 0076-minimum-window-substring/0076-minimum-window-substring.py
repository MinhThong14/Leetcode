class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        l, r = 0, 0

        dict_t = Counter(t)

        required = len(dict_t)

        window_s = {}

        formed = 0

        ans = float("inf"), None, None

        while r < len(s):
            char = s[r]
            window_s[char] = window_s.get(char, 0) + 1

            if char in dict_t and window_s[char] == dict_t[char]:
                formed += 1
            
            while l <= r and formed == required:
                char = s[l]

                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                
                window_s[char] -= 1
                if char in dict_t and window_s[char] < dict_t[char]:
                    formed -= 1
                
                l += 1
            r += 1
        
        return "" if ans[0] == float('inf') else s[ans[1]: ans[2]+1]

