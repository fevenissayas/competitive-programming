class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        val = sum(nums[:k])
        store = val
        for i in range (k, len(nums)):
            val = val + nums[i] - nums[i-k]
            store = max (store, val)
        
        return store/k