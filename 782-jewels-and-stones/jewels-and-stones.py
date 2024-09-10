class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        seen = set(jewels)
        return sum(i in seen for i in stones)