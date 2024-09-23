class Solution:
    def helper(self, s, indx):
        if indx == len(s)//2:
            return
        s[indx], s[len(s)-indx-1] = s[len(s)-indx-1], s[indx]
        self.helper(s, indx+1)
        
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.helper(s, 0)
        