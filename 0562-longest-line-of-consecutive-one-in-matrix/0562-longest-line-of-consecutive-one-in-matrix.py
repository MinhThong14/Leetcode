class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        
        max_len = 0
        
        m, n = len(mat), len(mat[0])
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    left_len = 1
                    l = j - 1
                    while l > -1 and mat[i][l] == 1:
                        left_len += 1
                        l -= 1
                    
                    right_len = 1
                    r = j + 1
                    while r < n and mat[i][r] == 1:
                        right_len += 1
                        r += 1
                    
                    above_len = 1
                    abv = i-1
                    while abv > - 1 and mat[abv][j] == 1:
                        above_len += 1
                        abv -= 1
                    
                    below_len = 1
                    bel = i+1
                    while bel < m and mat[bel][j] == 1:
                        below_len += 1
                        bel += 1
                    
                    diag_right_len = 1
                    x_r_diag = i+1
                    y_r_diag = j+1
                    while x_r_diag < m and y_r_diag < n and mat[x_r_diag][y_r_diag] == 1:
                        x_r_diag += 1
                        y_r_diag += 1
                        diag_right_len += 1
                    
                    diag_left_len = 1
                    x_l_diag = i-1
                    y_l_diag = j-1
                    while x_l_diag > -1 and y_l_diag > -1 and mat[x_l_diag][y_l_diag] == 1:
                        x_l_diag -= 1
                        y_l_diag -= 1
                        diag_left_len += 1
                    
                    anti_diag_left_len = 1
                    anti_x_l_diag = i+1
                    anti_y_l_diag = j-1
                    while anti_x_l_diag < m and anti_y_l_diag > -1 and mat[anti_x_l_diag][anti_y_l_diag] == 1:
                        anti_x_l_diag += 1
                        anti_y_l_diag -= 1
                        anti_diag_left_len += 1
                    
                    anti_diag_right_len = 1
                    anti_x_r_diag = i-1
                    anti_y_r_diag = j+1
                    while anti_x_r_diag > -1 and anti_y_r_diag < n and mat[anti_x_r_diag][anti_y_r_diag] == 1:
                        anti_x_r_diag -= 1
                        anti_y_r_diag += 1
                        anti_diag_right_len += 1
                    
                    max_len = max(max_len, left_len, right_len, above_len, below_len, diag_right_len, diag_left_len, anti_diag_left_len, anti_diag_right_len)
        
        return max_len
                        