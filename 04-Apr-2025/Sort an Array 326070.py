# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(nums):
            if len(nums) == 1:
                return nums
            
            mid = len(nums)//2
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])
            return merge(left, right)
        
        def merge(left, right):
            ans = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    ans.append(left[i])
                    i += 1
                else:
                    ans.append(right[j])
                    j += 1
            
            ans.extend(left[i:])
            ans.extend(right[j:])
            
            return ans
        
        return merge_sort(nums)