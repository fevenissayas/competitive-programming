# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        lst = []
        for i in count:
            if count[i] == 2:
                lst.append(i)
        return lst