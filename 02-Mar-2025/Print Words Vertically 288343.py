# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_length = 0
        for word in words:
            max_length = max(max_length, len(word))
        
        ans = []
        for i in range(max_length):
            chars = []
            for word in words:
                if i < len(word):
                    chars.append(word[i])
                else:
                    chars.append(' ')
          
            while chars and chars[-1] == ' ':
                chars.pop()
          
            ans.append(''.join(chars))
      
        return ans