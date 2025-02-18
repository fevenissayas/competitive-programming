# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        lst = [0]*(max(nums) - min(nums) + 1)
        minn = min(nums)
        for elem in nums:
            lst[elem-minn] += 1
        
        so_lst = []
        for i in range(len(lst)):
            while lst[i] != 0:
                so_lst.append(i+minn)
                lst[i] -= 1

        return so_lst