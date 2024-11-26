from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_count = Counter(ransomNote)
        m_count = Counter(magazine)
        for i, val in r_count.items():
            if m_count[i] < val:
                return False
        return True