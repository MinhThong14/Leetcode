class Solution:
    def inverseRows(self, matrix):
        m = len(matrix)
        
        for i in range(m//2):
            for j in range(m):
                matrix[i][j], matrix[m-i-1][j] = matrix[m-i-1][j], matrix[i][j]
        return matrix
    
    def diagnoseMatrix(self, matrix):
        
        n = len(matrix)
        
        for i in range(n):
            for j in range(i+1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix

            
    
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        matrix = self.inverseRows(matrix)
        matrix = self.diagnoseMatrix(matrix)
        return matrix