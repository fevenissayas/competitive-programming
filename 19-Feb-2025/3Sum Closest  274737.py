# Problem: 3Sum Closest  - https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        close_sum = float('inf')
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            while l < r:
                summ = nums[i] + nums[l] + nums[r]
                if summ == target:
                    return target
                elif abs(target - summ) < abs(target - close_sum):
                    close_sum = summ
                elif summ  < target:
                    l += 1
                else:
                    r -= 1

        return close_sum