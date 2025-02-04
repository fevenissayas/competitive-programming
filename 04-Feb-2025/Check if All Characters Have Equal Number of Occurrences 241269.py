# Problem: Check if All Characters Have Equal Number of Occurrences - https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = Counter(s)
        for i in range(len(s)-1):
            if count[s[i]] != count[s[i+1]]:
                return False
        return True