# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[-1])
        stack = []
        sign = {'*', '/', '+', '-'}
        ans = 0
        for i in range(len(tokens)):
            if tokens[i] not in sign:
                stack.append(tokens[i])
            else:
                ans = stack.pop()
                ans = int(eval(stack.pop() + tokens[i] + ans))
                stack.append(str(ans))

        return ans     
