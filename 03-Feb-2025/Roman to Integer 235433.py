# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1, 'V':5, 'X':10, 'L': 50, 'C':100, 'D':500, 'M':1000}
        summ = 0
        for i in range(len(s)):
            if i < len(s) - 1 and dic[s[i]] < dic[s[i+1]]:
                summ -= dic[s[i]]
            else:
                summ += dic[s[i]]
                
        return summ