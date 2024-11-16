class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, len(nums) - 1
        p = 0
        while p <= j:
            if nums[p] == 0:
                nums[p], nums[i] = nums[i], nums[p]
                i += 1
                p += 1
            elif nums[p] == 2:
                nums[p], nums[j] = nums[j], nums[p]
                j -= 1
            else:
                p += 1