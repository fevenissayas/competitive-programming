# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set(nums)
        for i in range(len(nums)+1):
            if i not in s:
                return i