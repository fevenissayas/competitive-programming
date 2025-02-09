# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_ = {}

        for elem in strs:
            so = ''.join(sorted(elem))
            if so in dict_:
                dict_[so].append(elem)
            else:
                dict_[so] = [elem]

        return list(dict_.values())