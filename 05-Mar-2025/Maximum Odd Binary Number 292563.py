# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        one = s.count('1')
        zero = len(s)-one
        return '1'*(one-1) + '0'*zero + '1'