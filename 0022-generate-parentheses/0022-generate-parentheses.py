class Solution:
    def backtracking(self, cur_string, left, right, n, answer):
        if len(cur_string) == 2 * n:
            answer.append(''.join(cur_string))
            return
        
        if left < n:
            cur_string.append('(')
            self.backtracking(cur_string, left+1, right, n, answer)
            cur_string.pop()
        if right < left:
            cur_string.append(')')
            self.backtracking(cur_string, left, right+1, n, answer)
            cur_string.pop()
        
    
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        
        self.backtracking([], 0, 0, n, answer)
        
        return answer
        
        