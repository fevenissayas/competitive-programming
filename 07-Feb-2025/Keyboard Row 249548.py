# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        lst = []
        row1 = set('qwertyuiop')
        row2 = set('asdfghjkl')
        row3 = set('zxcvbnm')

        for items in words:
            if items[0].lower() in row1:
                check = row1
            elif items[0].lower() in row2:
                check = row2
            elif items[0].lower() in row3:
                check = row3

            flag = True
            for char in items:
                if char.lower() not in check:
                    flag = False
                    break
            if flag:
                lst.append(items)

        return lst