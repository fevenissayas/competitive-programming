class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0
        emp = 0
        while numBottles > 0:
            res += numBottles
            emp += numBottles
            numBottles = emp//numExchange
            emp = emp % numExchange

        return res