# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for elem in logs:
            if elem == "./":
                continue
            elif elem != "../":
                stack.append(elem)
            else:
                if stack:
                    stack.pop()

        return len(stack)