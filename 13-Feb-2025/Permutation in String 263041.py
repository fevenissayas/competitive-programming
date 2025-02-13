# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        count1 = Counter(s1)
        count2 = Counter(s2[:n])
        if count1 == count2:
                return True

        for i in range(n, len(s2)):
            count2[s2[i]] += 1
            count2[s2[i-n]] -= 1
            if count2[s2[i-n]] == 0:
                del (count2[s2[i-n]])

            if count1 == count2:
                return True

        return False