class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        
        while n:
            most_left_bit = n & 1
            if most_left_bit == 1:
                count += 1
            n >>= 1
        
        return count