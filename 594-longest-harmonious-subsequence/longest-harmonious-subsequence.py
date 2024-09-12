class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        maxi = 0
        for i, val in count.items():
            if (i + 1) in count:
                maxi = max(maxi, count[i + 1] + val)
        
        return maxi