# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        lst = []
        
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(matrix[j][i])
            lst.append(temp)

        return lst