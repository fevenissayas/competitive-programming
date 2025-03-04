# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = sorted(costs, key = lambda x: x[0] - x[1])
        n = len(costs)//2
        min_sum = 0
        for i in range(n):
            min_sum += diff[i][0]

        for i in range(n, len(costs)):
            min_sum += diff[i][1]

        return min_sum