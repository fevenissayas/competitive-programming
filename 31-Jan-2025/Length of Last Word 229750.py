# Problem: Length of Last Word - https://leetcode.com/problems/length-of-last-word/description/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.strip()
        if " " not in x:
            return len(x)
        count = 0
        for i in range(len(x)-1, -1, -1):
            if x[i] == " ":
                return count
            count += 1