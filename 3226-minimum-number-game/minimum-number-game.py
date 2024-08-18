class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        i = 0
        while i < len(nums):
            nums[i+1], nums[i] = nums[i], nums[i+1]
            i += 2
        return nums