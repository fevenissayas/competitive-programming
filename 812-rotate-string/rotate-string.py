class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal:
            return True
        count = 1
        while count < len(goal):
            s += s[count-1]
            if goal == s[count:]:
                return True
            count += 1
        
        return False