# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        count = 0
        i, j = 0, len(s)-1

        def check(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i+=1
                j-= 1
            return True
        
        while i < j:
            if s[i] != s[j]:
                return check(i+1, j) or check(i, j-1)
    
            i+=1
            j-=1

        return True