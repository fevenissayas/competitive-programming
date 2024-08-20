class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = 0
        for i in range(k):
            n += nums[i]
        val = n / k
        for i in range(k, len(nums)):
            n += nums[i] - nums[i - k]
            val = max(val, n / k)
        return val 