class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elem = sum(nums)
        dig = 0
        for i in nums:
            for j in str(i):
                dig = dig + int(j)

        return elem - dig       