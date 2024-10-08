class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        
        x = ""
        
        start = min(n, m)
            
        while start > 0:
            sub_string = str1[:start]
            if str1 == (n // len(sub_string)) * sub_string and str2 == (m // len(sub_string)) * sub_string:
                return sub_string
            start -= 1

    
        return ""
            