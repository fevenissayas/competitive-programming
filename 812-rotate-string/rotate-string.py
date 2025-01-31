class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        count = 0
        while count < len(goal):
            s += s[count]
            if goal == s[count+1:]:
                return True
            count += 1
        
        return False