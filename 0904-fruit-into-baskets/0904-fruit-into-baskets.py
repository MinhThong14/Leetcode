class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        
        l, r = 0, 0
        n = len(fruits)
        res = 0
        
        while r < n:
            fruit = fruits[r]
            if fruit not in basket:
                basket[fruit] = 0
            basket[fruit] += 1
            
            while len(basket) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    basket.pop(fruits[l])
                l += 1
            
            res = max(res, sum(basket.values()))
            r += 1
        
        return res
                