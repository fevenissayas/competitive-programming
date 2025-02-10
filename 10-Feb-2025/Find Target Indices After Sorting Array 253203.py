# Problem: Find Target Indices After Sorting Array - https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        lst = []
        nums.sort()
        for i, elem in enumerate(nums):
            if elem == target:
                lst.append(i)
                
        return lst