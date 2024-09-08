class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def capitalize(window):
            low = set()
            up = set()
            for i in window:
                if i.isupper():
                    up.add(i)
                else:
                    low.add(i)

            for i in low:
                if i.upper() not in up:
                    return False
            for i in up:
                if i.lower() not in low:
                    return False
            return True

        maxi = ""
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                window = s[i:j+1]
                if capitalize(window) and len(maxi) < len(window):
                    maxi = window
        return maxi