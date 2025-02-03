# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strr = ""
        for i in digits:
            strr += str(i)
        val = int(strr)+1

        return list(map(int, str(val)))