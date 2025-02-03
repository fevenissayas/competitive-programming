# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left, right+1):
            flag = True
            for j in range(len(ranges)):
                if ranges[j][0] <= i <= ranges[j][-1]:
                    flag = False
                    break
            if flag:
                return False

        return True