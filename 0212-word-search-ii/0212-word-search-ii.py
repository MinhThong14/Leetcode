class Trie:
    
    def __init__(self):
        self.child = {}
        
    def insert(self, word):
        current = self.child
        
        for w in word:
            if w not in current:
                current[w] = {}
            current = current[w]
        
        current['#'] = {}
    
    def search(self, word):
        current = self.child
        
        for w in word:
            if w not in current:
                return False
            current = current[w]
        
        return '#' in current
    
    def isPrefix(self, word):
        current = self.child
        
        for w in word:
            if w not in current:
                return False
            current = current[w]
        
        return True
    
    def remove(self, word):
        cur_node = self. child
        nodes = []
        for w in word:
            if w not in cur_node:
                return
            cur_node = cur_node[w]
            nodes.append((cur_node, w))
        

        if '#' in cur_node:
            p = '#'
            for n, w, in nodes[::-1]:
                if p == '#' or len(n[p]) == 0:
                    del n[p]
                p = w

        


class Solution:
    def adj(self, x, y, m, n):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        adjacents = []
        
        for i, j in directions:
            if 0 <= x + i < m and 0 <= y + j < n:
                adjacents.append((x+i, y+j))
        return adjacents
    
    def dfs(self, word, board, word_dict, x, y, m, n, res):
        char, board[x][y] = board[x][y], '#'
        
        if word_dict.search(word):
            res.add(word)
            word_dict.remove(word)
        
        for i, j in self.adj(x, y, m, n):
            if board[i][j] != '#':
                new_word = word + board[i][j]
                if word_dict.isPrefix(word):
                    self.dfs(new_word, board, word_dict, i, j, m, n, res)
        
        board[x][y] = char
        
    
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        word_dict = Trie()
        res = set()
             
        for word in words:
            word_dict.insert(word)
        
        
        m, n = len(board), len(board[0])
        
        for i in range(m):
            for j in range(n):
                self.dfs(board[i][j], board, word_dict, i, j, m, n, res)
                
        return res

                