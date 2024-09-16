class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        s_stack = []
        t_stack = []
        
        n = len(s)
        
        cur_s_indx = 0
        while cur_s_indx < n:
            idx = cur_s_indx
            while idx < n and s[idx] == '#':
                if s_stack:
                    s_stack.pop(-1)
                idx += 1
            if idx != cur_s_indx:
                cur_s_indx = idx
            else:
                s_stack.append(s[cur_s_indx])
                cur_s_indx += 1
        
        cur_t_indx = 0
        m = len(t)
        while cur_t_indx < m:
            idx = cur_t_indx
            while idx < m and t[idx] == '#':
                if t_stack:
                    t_stack.pop(-1)
                idx += 1
            if idx != cur_t_indx:
                cur_t_indx = idx
            else:
                t_stack.append(t[cur_t_indx])
                cur_t_indx += 1
        
        return s_stack == t_stack
        
        
            
                
                
        
        