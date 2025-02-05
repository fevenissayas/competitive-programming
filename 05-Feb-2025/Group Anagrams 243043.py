# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for elem in strs:
            so = ''.join(sorted(elem))
            dic[so].append(elem)

        return list(dic.values())