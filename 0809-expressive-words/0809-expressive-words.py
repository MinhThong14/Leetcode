class Solution:
    
    def validate_string(self, s, word):
        count = 0
        
        m, n = len(s), len(word)
        
        if m < n:
            return 0
        
        l, r = 0, 0
        
        i = 0
        
        while l < m and i < n:
            if s[l] != word[i]:
                # print(s[l])
                # print(word[i])
                return 0
            
            while r < m and s[l] == s[r]:
                count += 1
                r += 1

            count_dup = 1
            while i < n-1 and word[i] == word[i+1]:
                count_dup += 1
                i += 1
            if (count < 3 and count_dup != count) or (count_dup > count):
                return 0
        
            i += 1
            l = r
            count = 0
            count_dup = 0
            # print(count)
            # print(count_dup)
            # print()
            
                          
        return 1 if l == m and i == n else 0 
    
    def expressiveWords(self, s: str, words: List[str]) -> int:
        
        num_words = 0
        
        for word in words:
            if self.validate_string(s, word) == 1:
                num_words += 1
            # print()
            # print(num_words)
            # print(word)
            # print()
        
        return num_words