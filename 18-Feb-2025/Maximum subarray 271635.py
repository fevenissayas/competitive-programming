# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            maxx = max(maxx+nums[i], nums[i])
            ans = max(ans, maxx)

        return ans