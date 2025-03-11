# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for char in s:
            print(stack)
            if char == '(':
                stack.append(0)
            else:
                val = stack.pop()
                score = max(2 * val, 1)
                stack[-1] += score
        
        return stack[0]
