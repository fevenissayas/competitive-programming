# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0]*len(s)
        for l,r,d in shifts:
            if d == 0:
                prefix[l] -= 1
                if r+1 < len(s):
                    prefix[r+1] += 1

            else:
                prefix[l] += 1
                if r+1 < len(s):
                    prefix[r+1] -= 1

        for i in range(1, len(prefix)):
            prefix[i] += prefix[i-1]
        
        ans = []
        for i in range(len(s)):
            shift = prefix[i]%26
            val = ord(s[i]) + shift
            if val > 122:
                val -= 26
            if val < 97:
                val += 26
            
            ans.append(chr(val))

        return ''.join(ans)

