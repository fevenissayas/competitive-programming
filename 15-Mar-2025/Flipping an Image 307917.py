# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        
        for elem in range(n):
            image[elem] = image[elem][::-1]
            for i in range(m):
                image[elem][i] ^= 1

        return image