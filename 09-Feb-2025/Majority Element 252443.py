# Problem: Majority Element - https://leetcode.com/problems/majority-element/description/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        for elem in count:
            if count[elem] > len(nums)//2:
                return elem