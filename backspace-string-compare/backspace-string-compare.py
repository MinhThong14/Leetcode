class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        s_stack = []
        t_stack = []
        
        m, n = len(s), len(t)
        
        i, j = 0, 0
        
        while i < m:
            while i < m and s[i] == '#':
                if s_stack:
                    s_stack.pop()
                i += 1
            if i < m:
                s_stack.append(s[i])
            i += 1
        
        while j < n:
            while j < n and t[j] == '#':
                if t_stack:
                    t_stack.pop()
                j += 1
            
            if j < n:
                t_stack.append(t[j])
            j += 1
        
        return s_stack == t_stack
        
        
            
                
                
        
        