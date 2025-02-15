# Problem: Longest Subarray of 1's After Deleting One Element - https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero = 0
        j = 0
        val = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1 
            while zero > 1:
                if nums[j] == 0:
                    zero -= 1
                j += 1
            val = max(val, i-j)
        return val