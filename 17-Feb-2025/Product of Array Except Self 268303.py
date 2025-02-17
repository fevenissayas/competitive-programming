# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lst = [1]*len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            lst[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            lst[i] *= suffix
            suffix *= nums[i]

        return lst