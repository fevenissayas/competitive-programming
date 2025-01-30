# Problem: Palindrome Number  - https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = x
        temp = 0
        while x > 0:
            rem = x % 10
            temp = temp * 10 + rem
            x //= 10
        return y == temp