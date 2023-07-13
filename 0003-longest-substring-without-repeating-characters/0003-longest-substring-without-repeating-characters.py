class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1

        max_length = 0
        while r <= len(s):
            sub_string = s[l:r]
            if r < len(s) and s[r] not in sub_string:
                sub_string += s[r]
            elif r < len(s) and s[r] in sub_string:
                l += 1
                continue

            max_length = max(max_length, len(sub_string))
            r += 1
        
        return max_length