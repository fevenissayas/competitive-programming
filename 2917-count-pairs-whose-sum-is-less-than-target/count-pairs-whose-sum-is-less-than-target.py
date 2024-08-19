class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        val = 0
        while i < j:
            if nums[i] + nums[j] >= target:
                j -= 1
            else:
                val += j - i
                i += 1
        return val