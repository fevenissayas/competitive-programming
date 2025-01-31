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