"""
424. Longest Repeating Character Replacement
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length

ABAB
k=2
l= 0, r = 1 -> sub_str = 'A' -> hashset = {'A':1} -> k=2 -> res = 1
l=0 , r = 2 -> sub_str = 'AB' -> hashset = {'A': 1 'B':1} -> k=1 -> res = 2
l=0 , r = 3 -> sub_str = 'ABA' -> hashset = {'A':2 'B':1} -> k=1 -> res = 3


AABABBA
k=1
l= 0, r = 1 -> sub_str = 'A' -> hashset = {'A':1} -> k=1 -> res = 1
l= 0, r = 2 -> sub_str = 'AA' -> hashset = {'A':2} -> k=1 -> res = 2
l= 0, r = 3 -> sub_str = 'AAB' -> hashset = {'A':2, 'B':1} -> k=0 -> res = 3
l= 0, r = 4 -> sub_str = 'AABA' -> hashset = {'A':3, 'B':1} -> k=0 -> res = 4
l= 0, r = 5 -> sub_str = 'AABAB' -> hashset = {'A':3, 'B':2} -> k=-1 -> res = 4
     l = 1, r = 5 -> sub_str = 'ABAB' -> hashset = {'A':2, 'B':2} -> k=1 < 2 -> res = 4
     l = 2, r = 5 -> sub_str = 'BAB' -> hashset = {'A':1, 'B':2} -> k=0 -> res = 4 

k=2
ABBBC -> hashset = {'A':1 'B':3, 'C':1} -> sub_str.len() - max_value = 5-3 = 2 <= 2

Time: O(N^2)
Space: O(N)

"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
#          create pointers
        l, r = 0, 0
#     create hashset
        hashset = defaultdict(int)
        # hashset[s[l]] = 1
        
        n = len(s)
        
        res = float('-inf')
        
#         while l < n and r < n:
#             cur_len = r - l + 1
            
#             cur_max_value = max(hashset.values())
            
#             if cur_len - cur_max_value <= k:
#                 res = max(res, cur_len)
#                 r += 1
#                 if r < n:
#                     hashset[s[r]] += 1
#             else:
#                 if l < n:
#                     hashset[s[l]] -= 1
#                 l += 1

        for r in range(n):
            cur_len = r - l + 1
            hashset[s[r]] += 1
            
            cur_max_value = max(hashset.values())
            
            if cur_len - cur_max_value <= k:
                res = max(res, cur_len)
            
            while cur_len - cur_max_value > k:
                hashset[s[l]] -= 1
                l += 1
                cur_len = r - l + 1
                cur_max_value = max(hashset.values())
            
        return res
            
            
            
            