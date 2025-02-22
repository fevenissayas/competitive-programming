# Problem: Sorting the Sentence - https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split()
        arr2 = ['']*len(arr)
        for i in arr:
            arr2[int(i[-1])-1] = i[:-1]
        return (' '.join(arr2))