# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = Counter()
        ans = 0
        for right in range(len(s)):
            count[s[right]] += 1
            if count['L'] == count['R']:
                ans += 1
                count = Counter()

        return ans