
class Trie:

    def __init__(self):
        self.child = {}
        

    def insert(self, word: str) -> None:
        current = self.child
        
        for w in word:
            if w not in current:
                current[w] = {}
            current = current[w]
        
        current['#'] = {}
        
    def search(self, word: str) -> bool:
        
        current = self.child
        
        for w in word:
            if w not in current:
                return False
            current = current[w]
        
        return True if '#' in current else False
        

    def startsWith(self, prefix: str) -> bool:
        
        current = self.child
        
        for w in prefix:
            if w not in current:
                return False
            current = current[w]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)