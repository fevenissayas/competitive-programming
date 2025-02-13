# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        area = 0

        while i < j:
            curr_area = (j-i) * min(height[i], height[j])
            area = max(area, curr_area)

            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
            
        return area