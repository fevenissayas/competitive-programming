class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        seen = set(jewels)
        for i in stones:
            if i in seen:
                count += 1
        return count