# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        last = nums[-1]

        i = len(nums)-1
        while i > 1:
            if nums[i-1] + nums[i-2] <= nums[i]:
                i -= 1
            else:
                return nums[i-1] + nums[i-2] + nums[i]
            
        return 0
