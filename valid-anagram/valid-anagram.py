class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_counter = Counter(s)
        t_counter = Counter(t)
        
        
        for k, val in s_counter.items():
            if t_counter[k] != val:
                return False
        
        return True