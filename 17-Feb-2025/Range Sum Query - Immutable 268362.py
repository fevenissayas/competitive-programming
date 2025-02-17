# Problem: Range Sum Query - Immutable - https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        temp = 0
        self.prefix = [0]*(len(nums)+1)
        for i in range(len(nums)):
            temp += nums[i]
            self.prefix[i+1] = temp     

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1] - self.prefix[left]

