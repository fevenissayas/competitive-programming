class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        maxi = ""
        for i in range(len(s)):
            low = set()
            up = set()
            for j in range(i, len(s)):
                char = s[j]
                if char.islower():
                    low.add(char)
                else:
                    up.add(char)
                
                if (char.isupper() and char.lower() not in low) or (char.islower() and char.upper() not in up):
                    continue
                if len(low) == len(up) and all(c.upper() in up for c in low):
                    if len(maxi) < len(s[i:j+1]):
                        maxi = s[i:j+1]
        
        return maxi