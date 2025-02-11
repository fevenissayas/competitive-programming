# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = deque(sorted(piles))
        lst = []

        while piles:
            piles.pop()
            lst.append(piles[-1])
            piles.pop()
            piles.popleft()
        
        return sum(lst)