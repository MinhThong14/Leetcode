class Solution:
    def reverse(self, digits):
        l, r = 0, len(digits)-1
        while l < r:
            digits[l], digits[r] = digits[r], digits[l]
            l += 1
            r -= 1
        
    def plusOne(self, digits: List[int]) -> List[int]:
        
        self.reverse(digits)
        print(digits)
        
        n = len(digits)
        
        carry = 1
        for i in range(n):
            cur_sum = digits[i] + carry
            
            if cur_sum > 9:
                carry = 1
            else:
                carry = 0
            
            cur_digit = cur_sum % 10 
            digits[i] = cur_digit
        
        if carry == 1:
            digits.append(1)
        
        self.reverse(digits)
        
        return digits