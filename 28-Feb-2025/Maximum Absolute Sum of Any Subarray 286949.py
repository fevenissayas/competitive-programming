# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxx = -inf
        minn = inf
        val = curr = 0

        for num in nums:
            curr = max(num, curr+num)
            maxx = max(curr, maxx)    
            val = min(num, val+num)
            minn = min(val, minn)
        
        maxx = max(abs(maxx), abs(minn))

        return maxx