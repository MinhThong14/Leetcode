
class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        
        n = len(s)
        
        for i in range(n):
            if (s[i] == ']'):
                decodedString = []
                
                while stack[-1] != '[':
                    decodedString.append(stack.pop())
                    
                stack.pop()
                base = 1
                k = 0
                
                while stack and stack[-1].isnumeric():
                    k += int(stack.pop()) * base
                    base *= 10
                
                while k != 0:
                    for j in range(len(decodedString)-1, -1, -1):
                        stack.append(decodedString[j])
                    k -= 1
                
            else:
                stack.append(s[i])
        
        return ''.join(stack)
                
                
                    