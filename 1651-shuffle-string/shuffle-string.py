class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        lst = [''] * (len(s))
        for i, val in enumerate(s):
            lst[indices[i]] = val

        return ''.join(lst)