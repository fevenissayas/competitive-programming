# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums)-1
        p = 0

        while p <= j:
            if nums[p] == 0:
                nums[i], nums[p] = nums[p], nums[i]
                i += 1
                p += 1

            elif nums[p] == 2:
                nums[p], nums[j] = nums[j], nums[p]
                j -= 1
            
            else:
                p += 1
