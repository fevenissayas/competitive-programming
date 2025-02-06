# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

from collections import Counter
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        c = 0
        t = 0

        for elem in count:
            c += count[elem]//2
            t += count[elem]%2
        return [c, t]
