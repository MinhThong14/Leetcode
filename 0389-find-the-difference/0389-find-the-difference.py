class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict = Counter(s)
        t_dict = Counter(t)
        
        for key, value in t_dict.items():
            if key not in s_dict or value > s_dict[key]:
                return key
    