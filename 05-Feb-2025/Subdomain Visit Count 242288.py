# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = defaultdict(int)
        ans = []

        for items in cpdomains:
            str1 = ""
            spl = items.split()
            dic[spl[1]] += int(spl[0])
            j = len(spl[-1]) - 1
            while j >= 0:
                if spl[1][j] == ".":
                    dic[str1] += int(spl[0]) 
                str1 = spl[1][j] + str1
                j -= 1
                
        for elem in dic:
            ans.append(f"{dic[elem]} {elem}")

        return ans