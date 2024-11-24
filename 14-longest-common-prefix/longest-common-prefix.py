class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_str = min(strs)
        for i in range(len(min_str)):
            for j in range(len(strs)):
                if strs[j][i] != min_str[i]:
                    return min_str[:i]
                    
        return min_str