class Solution:
    def numBits(self, i):
        
        count = 0
        
        while i:
            if i & 1:
                count += 1
            i >>= 1
        
        return count
        
    def countBits(self, n: int) -> List[int]:
        return [self.numBits(i) for i in range(n+1)]
