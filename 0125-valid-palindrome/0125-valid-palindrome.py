class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        
        palindrome = ''
        
        for char in s:
            if char.isalnum():
                palindrome += char.lower()
        
        l, r = 0, len(palindrome)-1
        
        while l < r:
            if palindrome[l] != palindrome[r]:
                return False
            l += 1
            r -= 1
        
        return True