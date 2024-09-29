class Solution:
    def isValid(self, s: str) -> bool:
        match = {")":"(", "}":"{", "]":"["}
        stack = []

        for i in s:
            if i in match.values():
                stack.append(i)
            elif i in match.keys():
                if not stack or match[i] != stack.pop():
                    return False
        
        return not stack