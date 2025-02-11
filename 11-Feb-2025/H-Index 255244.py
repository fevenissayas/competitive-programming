# Problem: H-Index - https://leetcode.com/problems/h-index/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()
        if sum(citations) == 0:
            return 0

        for i in range(n):
            if citations[i] > n-i-1:
                return n-i