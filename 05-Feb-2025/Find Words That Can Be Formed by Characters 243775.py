# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        summ = 0
        for elem in words:
            count = Counter(chars)
            for ind, j in enumerate(elem):
                if j not in count:
                    break
                else:
                    count[j] -= 1
                    if count[j] == 0:
                        del(count[j])
                        
                if ind == len(elem)-1:
                    summ += len(elem)

        return summ