class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = Counter(s)
        for char in t:
            if char not in s_count or s_count[char] == 0:
                return False
            else:
                s_count[char] -= 1
        
        return True

