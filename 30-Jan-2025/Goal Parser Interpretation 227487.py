# Problem: Goal Parser Interpretation - https://leetcode.com/problems/goal-parser-interpretation/description/

class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        dic = {"G":"G", "()":"o", "(al)":"al"}
        i = 0
        while i < len(command):
            strr = ""
            while strr not in dic:
                strr += command[i]
                i += 1
            ans += dic[strr]
        return ans