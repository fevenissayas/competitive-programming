class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        val = max(nums)
        for i in range(len(nums)):
            if nums[i] != val and nums[i]*2 > val:
                return -1
        return nums.index(val)