# Problem: Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        start_row = 0
        start_col = 0
        end_row = len(matrix) - 1
        end_col = len(matrix[0]) - 1

        ans = []
        while start_row <= end_row and start_col <= end_col:

            for i in range(start_col, end_col+1):
                ans.append(matrix[start_row][i])
            if len(ans) == len(matrix) * len(matrix[0]):
                break
            
            for j in range(start_row+1, end_row+1):
                ans.append(matrix[j][end_col])
            if len(ans) == len(matrix) * len(matrix[0]):
                break
            
            for i in range(end_col-1, start_col-1, -1):
                ans.append(matrix[end_row][i])
            if len(ans) == len(matrix) * len(matrix[0]):
                break

            for j in range(end_row-1, start_row, -1):
                ans.append(matrix[j][start_col])
            if len(ans) == len(matrix) * len(matrix[0]):
                break

            start_row += 1
            start_col += 1
            end_row -= 1
            end_col -= 1

        return ans