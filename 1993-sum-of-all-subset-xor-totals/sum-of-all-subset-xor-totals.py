class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        for num in nums:
            total |= num

        return total * (1 << (n-1))