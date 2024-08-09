class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        
        n = len(s)
        start = 0
        
        res = ""
        
        for i in range(n):
            if (s[i] == '('):
                stack.append(s[i])
            else:
                stack.pop()
            
            
            if len(stack) == 0:
                res += s[start+1:i]
                start = i + 1
        
        return res