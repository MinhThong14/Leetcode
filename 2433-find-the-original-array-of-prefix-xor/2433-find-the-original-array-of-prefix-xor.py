class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = [pref[0]]

        for i in range(1, len(pref)):
            cur_num = pref[i-1] ^ pref[i]
            res.append(cur_num)
        
        return res