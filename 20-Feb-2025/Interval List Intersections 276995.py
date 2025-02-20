# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        if firstList == [] or secondList == []:
            return []

        l1 = l2 = 0
        while l1< len(firstList) and l2<len(secondList):
            start1,end1 = firstList[l1]
            start2,end2 = secondList[l2]

            if start1 > end2:
                l2+=1
            elif start2 > end1:
                l1+=1

            else:
                result.append([max(start1,start2), min(end1,end2)])
                if end1>end2:
                    l2+=1
                else:
                    l1+=1

        return result