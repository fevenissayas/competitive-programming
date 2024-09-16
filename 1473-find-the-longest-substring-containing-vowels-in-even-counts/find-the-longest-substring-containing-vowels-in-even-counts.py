class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        occ = {0: -1}
        temp = maxi = 0

        for i, val in enumerate(s):
            if val in vowels:
                temp ^= vowels[val]
                
            if temp in occ:
                maxi = max(maxi, i - occ[temp])
            else:
                occ[temp] = i

        return maxi