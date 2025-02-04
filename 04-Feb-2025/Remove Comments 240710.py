# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        str1 = '""'.join(source)
        str2 = ""
        i = 0

        while i < len(str1):
            if i < len(str1) - 2 and str1[i] + str1[i+1] == '/*':
                i += 2
                while str1[i:i+2] != '*/':
                    i += 1
                i += 2
            elif i < len(str1) - 2 and str1[i] + str1[i+1] == '//':
                i += 2
                while str1[i:i+2] not in {'""', ""}:
                    i += 1
            else:
                str2 += str1[i]
                i += 1
        
        str2 = str2.split('""')
        ans = []

        for word in str2:
            if word:
                ans.append(word)

        return ans