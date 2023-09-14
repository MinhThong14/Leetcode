class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        for char in s:
            if char in ['(', '[', '{']:
                stack.append(char)
            elif stack:
                if char == ')' and stack[-1] == '(':
                    stack.pop()
                elif char == ']' and stack[-1] == '[':
                    stack.pop()
                elif char == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            else:
                return False
        
        return len(stack) == 0
                