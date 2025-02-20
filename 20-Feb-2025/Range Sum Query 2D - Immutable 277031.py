# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.sumMatrix = [[0]*(cols+1) for r in range(rows+1)]

        for row in range(rows):
            summ = 0
            for col in range(cols):
                summ += matrix[row][col]
                above = self.sumMatrix[row][col+1]
                self.sumMatrix[row+1][col+1] = summ + above
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottomright = self.sumMatrix[row2+1][col2+1]
        above = self.sumMatrix[row1][col2+1]
        left = self.sumMatrix[row2+1][col1]
        topleft = self.sumMatrix[row1][col1]        

        return bottomright-above-left+topleft

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
