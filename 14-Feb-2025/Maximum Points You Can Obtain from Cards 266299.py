# Problem: Maximum Points You Can Obtain from Cards - https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lst = cardPoints[-k:] + cardPoints[:k] 

        summ = 0
        for i in range(k):
            summ += lst[i]

        window = summ
        for i in range(k, len(lst)):
            summ += lst[i] - lst[i-k]
            window = max(window, summ)

        return window