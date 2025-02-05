# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        lst = []
        for i in count:
            if count[i] > len(nums)/3:
                lst.append(i)
        return lst