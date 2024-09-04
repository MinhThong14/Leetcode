class Solution:
    def combinations(self, digits, maps, cur_string, res):
        if len(digits) == 0:
            if cur_string:
                res.append(cur_string)
            
            return
        
        cur_letters = maps[digits[0]]
        
        for letter in cur_letters:
            cur_string += letter
            self.combinations(digits[1:], maps, cur_string, res)
            cur_string = cur_string[:-1]
        
        return
    
    def letterCombinations(self, digits: str) -> List[str]:
        maps = {"2":["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        
        res = []
        
        self.combinations(digits, maps, "", res)
        
        return res