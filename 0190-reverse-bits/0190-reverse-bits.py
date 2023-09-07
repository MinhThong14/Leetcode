class Solution:
    def reverseBits(self, n: int) -> int:
        l, r = 31, 0
        
        while l > r:
            i = 1 & (n >> l)
            j = 1 & (n >> r)
            
            if i != j:
                n ^= ((1 << l) | (1 << r))
            
            l -= 1
            r += 1
        
        return n