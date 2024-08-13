class Solution:
    def dfs(self, path, t, res):
        if path:
            res.add(path)
        
        for i in range(len(t)):
            self.dfs(path+t[i], t[:i]+t[i+1:], res)
        
        if not t:
            return
            
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()
        
        self.dfs("", tiles, res)
        
        return len(res)
        
        