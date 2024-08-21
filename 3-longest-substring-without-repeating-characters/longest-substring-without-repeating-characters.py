class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        j, k = 0, 0
        seen = set()
        for i in range(n):
            while s[i] in seen:
                seen.remove(s[j])
                j += 1
            seen.add(s[i])
            k = max(k, i - j + 1)
        return k