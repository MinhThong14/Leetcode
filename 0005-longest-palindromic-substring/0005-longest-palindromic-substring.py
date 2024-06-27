class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        
        for i in range(len(s)):
            l, r = i, i
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            cur_str = s[l+1:r]
            
            if i < len(s)-1:
                l1, r1 = i, i+1
            
                while l1 >= 0 and r1 < len(s) and s[l1] == s[r1]:
                    l1 -= 1
                    r1 += 1

                cur_str1 = s[l1+1:r1]


                if len(cur_str1) > len(cur_str):
                    cur_str = cur_str1

            
            if len(cur_str) > len(res):
                res = cur_str
            
        
        return res
                