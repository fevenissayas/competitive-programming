# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
            row = len(img)
            col = len(img[0])
            def inbound(i,j):
                return 0 <= i < row and 0 <= j < col
            
            direct = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

            smooth = []
            for i in range(row):
                new_row = []
                for j in range(col):
                    summ = img[i][j]
                    count_inbound = 1
                    for dx,dy in direct:
                        newR, newL = i + dx, j + dy
                        if inbound(newR,newL):
                            summ += img[newR][newL]
                            count_inbound += 1
                    
                    new_row.append(summ // count_inbound)
                smooth.append(new_row)

            return smooth