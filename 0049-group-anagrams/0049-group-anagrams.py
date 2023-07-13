class Solution:
    def groupAnagrams(self, strs):
        dict_t = collections.defaultdict(list)

        for string in strs:
            count = [0] * 26
            for c in string:
                count[ord(c) - ord('a')] += 1
            dict_t[tuple(count)].append(string)
        
        return dict_t.values()
                
        
