# Problem: Binary Search - https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while high>=low:
            mid = (high+low)//2
            if nums [mid] == target:
                return mid
            if nums [mid]>target:
                high = mid -1
            else:
                low = mid + 1
                
        return -1