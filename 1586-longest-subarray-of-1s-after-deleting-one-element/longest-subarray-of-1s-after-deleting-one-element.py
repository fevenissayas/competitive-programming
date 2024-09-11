class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero = 0
        j = 0
        val = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1 
            while zero > 1 and i >= j:
                if nums[j] == 0:
                    zero -= 1
                j += 1
            val = max(val, i-j)
        return val