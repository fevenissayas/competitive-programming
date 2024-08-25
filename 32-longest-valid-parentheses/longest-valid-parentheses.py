class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        L = 0

        for i in range(len(s)):
            if s[i] != "(":
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    L = max(L, i - stack[-1])
            else:
                stack.append(i)
  
        return L