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
        current = self.child
        node = []
        
        for w in word:
            if w not in current:
                return
            current = current[w]
            node.append((current, w))
        
        if '#' in current:
            p = '#'
            for n, w in node[::-1]:
                if p == '#' or not len(n[p]):
                    del n[p]
                p = w


    

class Solution:

    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        
        trie = Trie()
        res = set()
        
        for word in words:
            trie.insert(word)
        
        def adj(x, y):
            direcs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            
            for i, j in direcs:
                if 0 <= x+i < m and 0 <= y+j < n:
                    yield(x+i, y+j)
        
        def dfs(word, x, y):
            char, board[x][y] = board[x][y], '#'
            
            if trie.search(word):
                res.add(word)
                trie.remove(word)
            
            for i, j in adj(x, y):
                if board[i][j] != '#':
                    new_word = word + board[i][j]
                    if trie.isPrefix(new_word):
                        dfs(new_word, i, j)
            board[x][y] = char
        
        for i in range(m):
            for j in range(n):
                dfs(board[i][j], i, j)
        
                
        return res

                