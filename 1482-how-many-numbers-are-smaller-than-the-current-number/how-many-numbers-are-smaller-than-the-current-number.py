class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dic = {}
        for i, val in enumerate (sorted(nums)):
            if val not in dic:
                dic[val] = i
        return [dic[val] for val in nums]