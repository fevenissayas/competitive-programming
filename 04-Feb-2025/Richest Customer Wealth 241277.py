# Problem: Richest Customer Wealth - https://leetcode.com/problems/richest-customer-wealth/description/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum2 = 0
        for i in accounts:
            sum1 = sum(i)
            sum2 = max(sum1, sum2)
        return sum2