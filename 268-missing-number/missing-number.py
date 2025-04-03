class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        one = 0
        two = 0
        for i in range(len(nums)):
            two = two ^ nums[i]
            one = one ^ (i + 1)
        
        return one ^ two