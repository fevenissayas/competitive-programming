# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minn = min(strs)
        for i in range(len(minn)):
            for j in range(len(strs)):
                if minn[i] != strs[j][i]:
                    return minn[:i]

        return minn