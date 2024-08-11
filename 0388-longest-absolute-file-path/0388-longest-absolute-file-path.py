from collections import deque

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack  = deque()
        
        stack.append(0)
        max_len = 0
        
        for s in input.split("\n"):
            level = s.rfind("\t") + 1
            
            while level < len(stack) - 1:
                stack.pop()
            
            len_str = stack[-1] + (len(s) - level) + 1
            stack.append(len_str)
            
            if ("." in s):
                max_len = max(max_len, len_str - 1)
            
        
        return max_len