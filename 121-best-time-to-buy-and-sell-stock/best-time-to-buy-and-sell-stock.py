class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        j = None
        profit = 0
        
        for i in prices:
            if j is None:
                j = i
            elif i < j:
                j = i
            elif i - j > profit:
                profit = i - j
        
        return profit