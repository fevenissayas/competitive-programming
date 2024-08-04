class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = {}

        for i, j in enumerate(nums):
            if target - j in lst:
                return [i, lst[target - j]]
            lst[j] = i