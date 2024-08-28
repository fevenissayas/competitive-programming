class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        temp = sum(nums[:k])
        max_sum = temp
        for i in range(k, len(nums)): 
            temp += nums[i] - nums[i - k]
            max_sum = max(temp , max_sum)
        return max_sum/k