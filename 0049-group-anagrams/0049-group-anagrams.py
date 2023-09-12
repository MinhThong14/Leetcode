class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for string in strs:
            count = [0] * 26
            
            for c in string:
                count[ord(c) - ord('a')] += 1
            
            count = tuple(count)
            if count not in anagrams:
                anagrams[count] = []
            anagrams[count].append(string)
        
        return anagrams.values()