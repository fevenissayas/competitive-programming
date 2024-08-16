class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        data = Counter(nums)
        for i, val in data.items():
            if val >= 2:
                return i