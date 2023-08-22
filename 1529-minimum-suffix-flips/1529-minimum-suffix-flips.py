class Solution:
    def minFlips(self, target: str) -> int:
        count = 0
        prev = '0'
        for x in target:
            if x != prev:
                count += 1
                prev = x
        return count