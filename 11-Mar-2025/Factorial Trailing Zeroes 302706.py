# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        def factorial(n):
            if n == 1 or n == 0:
                return 1

            return n * factorial(n-1)
        
        count = 0
        val = factorial(n)
        rem = val%10
        while rem == 0:
            count += 1
            val //= 10
            rem = val%10

        return count
