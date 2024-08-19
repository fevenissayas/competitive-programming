class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        val = 0
        for i in range(1, len(points)):
            if val < (points[i][0] - points[i-1][0]):
                val = (points[i][0] - points[i-1][0])
        return val