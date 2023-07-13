class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = Counter(s)
        t_count = Counter(t)

        if len(s_count) != len(t_count):
            return False
        
        for k, value in s_count.items():
            if k not in t_count:
                return False
            elif value != t_count[k]:
                return False
        
        return True

