class Solution:
    def rotatedDigits(self, n: int) -> int:
        res = 0
        valid = {'0':'0', '1':'1', '8':'8', '2':'5', '5':'2', '6':'9', '9':'6'}
        
        for i in range(1, n+1):
            digits = str(i)
            map_digits = ""
            is_valid = True
            for j in range(len(digits)):
                if digits[j] in valid:
                    map_digit = valid[digits[j]]
                    map_digits += map_digit
                else:
                    is_valid = False
                    break
                    
            if is_valid:
                num = int(map_digits)
                if num != i:
                    res += 1

        return res