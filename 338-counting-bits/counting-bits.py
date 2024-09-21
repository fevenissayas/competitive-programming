class Solution:
    def countBits(self, n: int) -> List[int]:
        val = [0]*(n+1)
        i = 1
        while i <= n:
            t = min(i << 1, n)
            for j in range(i, t+1):
                val[j] = val[j-i] + 1
            i <<= 1
        return val