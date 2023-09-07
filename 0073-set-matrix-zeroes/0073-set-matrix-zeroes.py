class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        zero_row, zero_column = 0, 0
        
        m, n = len(matrix), len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        zero_row = 1
                    if j == 0:
                        zero_column = 1
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for k in range(1, m):
            for l in range(1, n):
                if matrix[k][0] == 0 or matrix[0][l] == 0:
                    matrix[k][l] = 0
        
        if zero_row:
            for w in range(n):
                matrix[0][w] = 0
        if zero_column:
            for h in range(m):
                matrix[h][0] = 0
        
        return matrix