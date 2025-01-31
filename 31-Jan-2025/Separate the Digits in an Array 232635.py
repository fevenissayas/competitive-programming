# Problem: Separate the Digits in an Array - https://leetcode.com/problems/separate-the-digits-in-an-array/description/

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        str1 = ""
        for i in nums:
            str1 += str(i)
        str1 = list(str1)
        for i in range(len(str1)):
            str1[i] = int(str1[i])
        return str1