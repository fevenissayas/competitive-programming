# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums2 = sorted(nums)
        dic = {}

        for i, val in enumerate(nums2):
            if val in dic:
                continue
            else:
                dic[val] = i
        
        for i in range(len(nums)):
            nums[i] = dic[nums[i]]
        
        return nums