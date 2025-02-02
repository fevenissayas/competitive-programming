# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        dic = {chr(i): i - 96 for i in range (97, 123)}
        trans = ""
        for i in s:
            trans += str(dic[i])
        
        for _ in range(k):
            summ = 0
            for i in range(len(trans)):
                summ += int(trans[i])
            trans = str(summ)
            
        return int(trans)