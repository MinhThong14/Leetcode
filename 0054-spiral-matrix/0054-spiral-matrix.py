class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        res = []
        l, r = 0, len(matrix[0])-1
        t, b = 0, len(matrix)-1

        while l <= r and t <= b:

            for i in range(l, r+1):
                res.append(matrix[t][i])
            
            t += 1
            if t > b:
                break
            
            for j in range(t, b+1):
                res.append(matrix[j][r])
            
            r -= 1
            if r < l:
                break

            for w in range(r, l-1, -1):
                res.append(matrix[b][w])
            
            b -= 1
            if b < t:
                break
            
            for g in range(b, t-1, -1):
                res.append(matrix[g][l])
            l += 1
            if l > r:
                break
        
        return res

