class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        seen = {'a', 'e', 'i', 'o', 'u'}
        for i in range(k):
            if s[i] in seen:
                count += 1
        count2 = count        
        for i in range(k, len(s)):      
            if s[i] in seen:
                count += 1 
            if s[i-k] in seen:
                count -= 1
            count2 = max(count, count2)
        return count2