# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        val = int(sqrt(c))  
        i = 0
        j = val

        while i <= j:
            if i**2 + j**2 > c:
                j -= 1
            
            elif i**2 + j**2 < c:
                i += 1
            
            else:
                return True
        
        return False