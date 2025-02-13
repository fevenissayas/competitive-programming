# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        val = 0
        for i in range(k):
            val += nums[i]

        max_sum = val
        for i in range(k, len(nums)):
            val += nums[i]-nums[i-k]
            max_sum = max(max_sum, val)
        
        return max_sum/k