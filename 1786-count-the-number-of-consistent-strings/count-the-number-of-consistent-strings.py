class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        seen = set(allowed)
        count = 0
        for i in words:
            if all(j in seen for j in i):
                count += 1
                    
        return count