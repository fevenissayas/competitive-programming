class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        dic = {}
        for i, num in enumerate(nums):
            dic[num] = i
        val = max(nums)
        for i in range(len(nums)):
            if nums[i] != val and nums[i]*2 > val:
                return -1
        return dic[val]