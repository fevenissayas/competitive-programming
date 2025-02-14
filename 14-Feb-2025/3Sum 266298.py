# Problem: 3Sum - https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lst = set()
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            while l < r:
                summ = nums[i]+nums[l]+nums[r]
                if summ == 0:
                    lst.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                else:
                    if summ > 0:
                        r -= 1
                    else:
                        l += 1
        lst = list(map(list,lst)) 
        return lst