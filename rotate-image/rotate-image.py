class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        t, b = 0, m-1
        
        while t < b:
            for i in range(n):
                matrix[t][i], matrix[b][i] = matrix[b][i], matrix[t][i]
            t += 1
            b -= 1
        
        for i in range(m):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        return matrix