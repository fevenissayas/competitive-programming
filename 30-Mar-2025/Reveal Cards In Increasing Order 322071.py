# Problem: Reveal Cards In Increasing Order - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        so = sorted(deck)
        deck = deque(range(len(deck)))
        ans = [0]*len(deck)
        order = []

        while deck:
            val = deck.popleft()
            order.append(val)
            if deck:
                deck.append(deck.popleft())

        for i, j in enumerate(order):
            ans[j] = so[i]
        
        return ans