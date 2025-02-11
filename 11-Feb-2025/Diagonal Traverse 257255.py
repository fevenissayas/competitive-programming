# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        dic = defaultdict(list)

        for i in range(m):
            for j in range(n):
                dic[i+j].append(mat[i][j])

        lst = []
        count = 0
        while count < m+n-1:
            if count % 2:
                lst.extend(dic[count])
            else:
                lst.extend(dic[count][::-1])
            count += 1
        
        return lst