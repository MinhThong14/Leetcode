class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        zero_row, zero_col = False, False

        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        zero_row = True
                    if j == 0:
                        zero_col = True
                    
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for g in range(1, m):
            for l in range(1, n):
                if matrix[g][0] == 0 or matrix[0][l] == 0:
                    matrix[g][l] = 0
        
        if zero_row:
            for c in range(n):
                matrix[0][c] = 0
        
        if zero_col:
            for r in range(m):
                matrix[r][0] = 0
        
        return matrix

