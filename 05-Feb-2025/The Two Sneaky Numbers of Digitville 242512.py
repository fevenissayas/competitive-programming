# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

from collections import Counter
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        count = Counter(nums)
        for i in count:
            if count[i] == 2:
                ans.append(i)
        return ans