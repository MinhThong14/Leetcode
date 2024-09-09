class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif not stack:
                return False
            else:
                if char == ')' and stack[-1] != '(':
                    return False

                elif char == '}' and stack[-1] != '{':
                    return False
                elif char == ']' and stack[-1] != '[':
                    return False

                stack.pop()
        
        return True if len(stack) == 0 else False                
        
        