from collections import defaultdict
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        temp = 0
        j = 0
        val = defaultdict(int)
        
        for i in range(len(s)):
            val[s[i]] += 1            
            while all(val[char] > 0 for char in "abc"):
                temp += len(s) - i
                val[s[j]] -= 1
                j += 1
        
        return temp