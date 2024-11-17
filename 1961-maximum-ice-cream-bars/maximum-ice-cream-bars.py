class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        summ = 0
        j = 0
        for i in range(len(costs)):
            summ += costs[i]            
            if summ > coins:
                return j
            j += 1
        return j