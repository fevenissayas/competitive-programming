from collections import Counter
from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        count = Counter()
        left = 0
        total = 0
        for i, val in enumerate(nums):
            count[val] += 1
            while len(count) > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1
            total += i - left + 1
        
        count2 = Counter()
        left2 = 0
        total2 = 0
        for i, val in enumerate(nums):
            count2[val] += 1
            while len(count2) > k - 1:
                count2[nums[left2]] -= 1
                if count2[nums[left2]] == 0:
                    del count2[nums[left2]]
                left2 += 1
            total2 += i - left2 + 1

        return total - total2