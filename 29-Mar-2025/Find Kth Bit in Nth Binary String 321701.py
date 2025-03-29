# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findStr(self, n):
        if n == 1:
            return [0]
        s1 = self.findStr(n-1)

        inv = []
        for i in s1:
            inv.append(1^i)
        
        return s1 + [1] + list(reversed(inv))

    def findKthBit(self, n: int, k: int) -> str:
        s = self.findStr(n)

        return str(s[k-1])