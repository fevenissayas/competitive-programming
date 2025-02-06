# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        set1 = {'+', '-', '(', ')', ' '}

        if s[0].isalpha():
            s = s.lower()
            i = 0
            while s[i+1] != '@':
                i += 1
                
            masked = s[0] + "*****" + s[i:]

        else:
            x = []
            for i in range(len(s)):
                if s[i] not in set1:
                    x.append(s[i])
            masked = "***-***-" + ''.join(x[-4:])
            if len(x) > 10:
                masked = '+' + '*'*(len(x)-10)+ '-' + masked

        return masked