# Problem: Largest Number - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        if sum(nums) == 0:
            return "0"

        for i in range(len(nums)):
            nums[i] = str(nums[i])
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            return 1

        x = sorted(nums, key=cmp_to_key(compare))
        return ''.join(x)