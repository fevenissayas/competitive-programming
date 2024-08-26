class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp = val = nums[0]
        for i in range(1, len(nums)):
            temp = max(nums[i], temp + nums[i])
            if temp > val:
                val = temp
        
        return val